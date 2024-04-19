from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def category(request, brandName):
    products = []
    for product in Car.objects.filter(car_brand=brandName):
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

def profile(request):
    context = {"is_authenticated": request.user.is_authenticated}
    if request.GET:
        pass
    else:
        if not request.user.is_authenticated:
            return redirect("/authentication/login")
        

        cars = Car.objects.filter(car_seller=request.user)
        carList = []
        for car in cars:
            carImage = CarImage.objects.filter(car_id=car)[0]
            carList.append([carImage.car_image.url,car])

        context["userData"] = request.user
        
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
        context["products"] = carList
    return render(request, "profile.html", context)

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