from django.shortcuts import render, redirect
from .models import *
from home.models import *
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.


def new_chat(request, user_id):
    try:
        if int(user_id) == request.user.pk:
            return redirect("/")
        else:
            user_get = User.objects.get(pk = int(user_id))
            room_filter = Room.objects.filter(user = request.user, user2 = user_get)
            if not room_filter:
                create_room = Room.objects.create(
                    user = request.user,
                    user2 = user_get,
                )
                create_room.save()

                create_room2 = Room.objects.create(
                    user = user_get,
                    user2 = request.user,
                )
                create_room2.save()

                return redirect(f"/chat/{create_room.pk}")
            else:
                return redirect(f"/chat/{room_filter[0].pk}")
    except:
        return redirect("/")

def chat(request, room_id=""):
    if not request.user.is_authenticated:
        return redirect("/authentication/login")
    
    if room_id != "":
        rend = "chat"
        try:
            room_get = Room.objects.get(pk = int(room_id), user=request.user)
            room_get.room_new_messages = 0
            room_get.save()
            chats = Chat.objects.filter(chat_room = room_get)
        except:
            return redirect("/authentication/login")
    else:
        rend = "chats"
        room_get = ""
        chats = ""
    
    rooms = Room.objects.filter(user = request.user)

    if request.method == "POST":
        a, errtitle = formChecker([
                [request.POST["messageInput"],1000,True,[
                        "يرجى كتابة الرسالة",
                        "الحد الأقصى للأحرف في الرسالة هي 1000 حرفًا"
                    ]
                ],
            ]
        )
        if a == "work":
            room_get2 = Room.objects.get(user=room_get.user2, user2 = request.user)

            chat_create = Chat.objects.create(
                chat_user = request.user,
                chat_room = room_get,
                chat_message = request.POST["messageInput"]
            )
            chat_create.save()

            chat_create = Chat.objects.create(
                chat_user = request.user,
                chat_room = room_get2,
                chat_message = request.POST["messageInput"]
            )

            room_get.room_last_message = request.POST["messageInput"]
            room_get2.room_last_message = request.POST["messageInput"]
            room_get.room_new_messages = room_get.room_new_messages + 1
            room_get2.room_new_messages = room_get2.room_new_messages + 1
            room_get.save()
            room_get2.save()
            chat_create.save()
        return JsonResponse({'errtitle':errtitle})
    elif "newMessages" in request.GET:
        print("asd")
        chatsList = []
        for chat in chats:
            chatsList.append(chat.chat_message)
        return JsonResponse({'chats':chatsList})
    
    favorites = Favorite.objects.filter(favorite_user=request.user)
    favoriteCount = len(favorites)

    notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
    notificationCount = len(notification)

    context = {
        "is_authenticated": request.user.is_authenticated,
        "favoriteCount": favoriteCount,
        "notificationCount": notificationCount,
        "rooms":rooms,
        "room_get":room_get,
        "chats":chats,
        "user":request.user
    }
    return render(request, f"{rend}.html", context)