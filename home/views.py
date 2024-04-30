from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse

# Create your views here.

def about(request):
    context = {
        "is_authenticated": request.user.is_authenticated,
    }
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
    return render(request, "about.html", context)

def category(request, brandName):
    products = []
    for product in Car.objects.filter(car_brand=brandName):
        car_image = CarImage.objects.filter(car_id = product)
        products.append([car_image[0].car_image.url,product])
    context = {
        "is_authenticated": request.user.is_authenticated,
        "products": products,
        "brandName":brandName
    }
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
    return render(request, "home.html", context)

def search(request,search):
    products = []
    brands = []
    if not request.GET:
        filterDB = Car.objects.filter(car_name__icontains = search)
    elif "carBrand" in request.GET:
        filterDB = Car.objects.filter(car_name__icontains = search, car_brand=request.GET["carBrand"])
    elif "low-to-high" in request.GET:
        filterDB = Car.objects.filter(car_name__icontains = search).order_by("-car_price")
    elif "high-to-low" in request.GET:
        filterDB = Car.objects.filter(car_name__icontains = search).order_by("car_price")
    for product in filterDB:

        if product.car_brand not in brands:
            brands.append(product.car_brand)
        car_image = CarImage.objects.filter(car_id = product)
        products.append([car_image[0].car_image.url,product])
    context = {
        "is_authenticated": request.user.is_authenticated,
        "search": search,
        "products": products,
        "brands":brands
    }
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
    return render(request, "search.html", context)

def home(request):
    products = []
    for product in Car.objects.all():
        car_image = CarImage.objects.filter(car_id = product)
        products.append([car_image[0].car_image.url,product])
    context = {
        "is_authenticated": request.user.is_authenticated,
        "products": products
    }
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
    return render(request, "home.html", context)

def components(request):
    context = {}
    return render(request, "components.html", context)

def edit_profile(request):
    context = {"is_authenticated": request.user.is_authenticated}
    if not request.user.is_authenticated:
        return redirect("/authentication/login")

    if request.method == "POST":
        a, errtitle = formChecker([
                [request.POST["firstName"],50,True,[
                        "يرجى ملئ جميع الحقول",
                        "الحد الأقصى للأحرف في الإسم الأول هو 50 حرفًا"
                    ]
                ],
                [request.POST["lastName"],50,True,[
                        "يرجى ملئ جميع الحقول",
                        "الحد الأقصى للأحرف في الإسم الأخير هو 50 حرفًا"
                    ]
                ],
                [request.POST["email"],75,True,[
                        "يرجى ملئ جميع الحقول",
                        "الحد الأقصى للأحرف في البريد الإلكتروني هو 75 حرفًا"
                    ]
                ],
            ]
        )
        if a == "work":
            if request.POST["email"] != request.user.email:
                emailFilter = User.objects.filter(email = request.POST["email"])
                if len(emailFilter) != 0:
                    a = "no"
                    errtitle = "البريد الإلكتروني مستخدم مسبقاً"
        if a == "work":
            user = request.user
            user.first_name = request.POST["firstName"]
            user.last_name = request.POST["lastName"]
            user.email = request.POST["email"]
            user.save()
        return JsonResponse({'errtitle':errtitle})
    
    favorites = Favorite.objects.filter(favorite_user=request.user)
    favoriteCount = len(favorites)

    notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
    notificationCount = len(notification)

    context["userData"] = request.user
    context["favoriteCount"] = favoriteCount
    context["notificationCount"] = notificationCount
    context["user"] = request.user
    return render(request, "edit-profile.html", context)

def profile(request):
    context = {"is_authenticated": request.user.is_authenticated}
    context["mainUser"] = request.user
    
    if "user_id" in request.GET:
        try:
            user = User.objects.get(pk = request.GET["user_id"])
        except:
            return redirect("/")
        cars = Car.objects.filter(car_seller=user)
        context["userData"] = user
    else:
        cars = Car.objects.filter(car_seller=request.user)
        context["userData"] = request.user
    carList = []
    for car in cars:
        carImage = CarImage.objects.filter(car_id=car)[0]
        carList.append([carImage.car_image.url,car])

    
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
    context["products"] = carList
    return render(request, "profile.html", context)

def ratings(request):
    if "user_id" in request.GET:
        pass
    else:
        return redirect("/")
    if request.user.is_authenticated: 
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)
    try:
        userData = User.objects.get(pk=request.GET["user_id"])
    except:
        return redirect("/")
    
    ratings = Rating.objects.filter(rate_user=userData)[::-1]

    context = {
        "ratings": ratings,
        "is_authenticated": request.user.is_authenticated
    }

    if request.method == "POST":
        a, errtitle = formChecker([
                [request.POST["content"],1000,True,[
                        "يرجى كتابة محتوى التقييم",
                        "الحد الأقصى للأحرف في عنوان التقييم هو 1000 حرفًا"
                    ]
                ],
            ]
        )

        if a == "work":
            if request.user.email != userData.email:
                notificationCreate = Notification.objects.create(
                    notification_user = userData,
                    notification_title = "تقييم جديد",
                    notification_description = "لقد تم تقييمك من قِبل عميل",
                    notification_link = f"/ratings?user_id={userData.pk}",
                )
                notificationCreate.save()
            rateCreate = Rating.objects.create(
                rate_sender = request.user,
                rate_user = userData,
                rate_content = request.POST["content"]
            )
        
        return JsonResponse({"errtitle":errtitle})
    
    context["userData"] = userData
    if request.user.is_authenticated:

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["mainUser"] = request.user
        context["notificationCount"] = notificationCount
    return render(request, "ratings.html", context)

def notifications(request):
    context = {
        "is_authenticated": request.user.is_authenticated
    }
    if not request.user.is_authenticated:
        return redirect("/authentication/login")


    favorites = Favorite.objects.filter(favorite_user=request.user)
    favoriteCount = len(favorites)

    notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
    notificationCount = len(notification)

    notifications = Notification.objects.filter(notification_user=request.user)[::-1]
    notificationsList = []
    for notification in notifications:
        notificationsList.append([notification.notification_title,notification.notification_description,notification.notification_link,notification.notification_is_new])

    context["userData"] = request.user
    context["favoriteCount"] = favoriteCount
    context["notificationCount"] = notificationCount
    context["notifications"] = notificationsList

    for notification in notifications:
        notification.notification_is_new = False
        notification.save()
    return render(request, "notifications.html", context)

def favorite(request):
    context = {
        "is_authenticated": request.user.is_authenticated
    }
    if not request.user.is_authenticated:
        return redirect("/authentication/login")
    
    favorite = Favorite.objects.filter(favorite_user=request.user)
    favoriteList = []
    for fav in favorite:
        favoriteImage = CarImage.objects.filter(car_id=fav.favorite_product)[0]
        favoriteList.append([favoriteImage.car_image.url,fav])

    favorites = Favorite.objects.filter(favorite_user=request.user)
    favoriteCount = len(favorites)

    notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
    notificationCount = len(notification)

    context["userData"] = request.user
    context["favoriteList"] = favoriteList
    context["favoriteCount"] = favoriteCount
    context["notificationCount"] = notificationCount
    return render(request, "favorite.html", context)