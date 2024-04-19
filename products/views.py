from django.shortcuts import render, redirect
from django.http import JsonResponse
from home.models import *
import re

regex = r'^(009665|9665|\+9665|05|5)(5|0|3|6|4|9|1|8|7)([0-9]{7})$'

def mobileValidation(phone_number):
    return bool(re.match(regex, phone_number))

# Create your views here.

def editProduct(request, product_id):
    try:
        product = Car.objects.get(pk=product_id,car_seller = request.user)
        car_image = CarImage.objects.filter(car_id=product)
        car_images = []
        for image in car_image:
            car_images.append(image)
        vehicleTypes = []
        if product.car_brand == "تويوتا":
            vehicleTypes.append('كامري')
            vehicleTypes.append('كورولا')
        elif product.car_brand == "هونداي":
            vehicleTypes.append('إكسنت')
            vehicleTypes.append('إلنترا')
        
        models = []
        if product.car_type == "كامري":
            models.append("GL")
            models.append("GL Limited")
            models.append("GL Standarnd")
            models.append("GLX")
            models.append("GLX Premium")
            models.append("GLX Sport Z")
            models.append("ستاندرد")
            models.append("جراندي")
        elif product.car_type == "كورولا":
            models.append("XLI")
            models.append("GLI")
            models.append("Sport 1.6")
            models.append("Limited 1.6")
            models.append("كروس هايبرد ستاندرد")
            models.append("كروس هايبرد نص فل")
            models.append("كروس هايبرد فل كامل")
        elif product.car_type == "إكسنت":
            models.append("GL")
            models.append("GLS")
            models.append("ستاندرد")
            models.append("فل كامل")
            models.append("نص فل")
        elif product.car_type == "إلنترا":
            models.append("فل كامل")
            models.append("ستاندرد")
            models.append("نص فل")
            models.append("بريميوم")
            models.append("ليميتد")
            models.append("ميد")
    except:
        return redirect('/')
    context = {
        "is_authenticated": request.user.is_authenticated,
        "product":product,
        "user":request.user,
        "vehicleTypes":vehicleTypes,
        "models":models,
        "years":range(2000,2025)[::-1],
        "car_images":car_images,
    }
    if request.method == "POST":
        a, errtitle = formChecker([
                [request.POST["title"],50,True,[
                        "يرجى ملئ جميع الحقول",
                        "الحد الأقصى للأحرف في عنوان الإعلان هو 50 حرفًا"
                    ]
                ],
                [request.POST["description"],1000,True,[
                        "يرجى ملئ جميع الحقول",
                        "الحد الأقصى للأحرف في الوصف هو 1000 حرفًا"
                    ]
                ],
                [request.POST["brand"],"select",True,[
                        "تويوتا",
                        "هونداي",
                    ]
                ],
                [request.POST["vehicleType"],"select",True,[
                        "كامري",
                        "كورولا",
                        "إكسنت",
                        "إلنترا",
                    ]
                ],
                [request.POST["model"],"select",True,[
                        "GL",
                        "GL Limited",
                        "GL Standarnd",
                        "GLX",
                        "GLX Premium",
                        "GLX Sport Z",
                        "ستاندرد",
                        "جراندي",
                        "XLI",
                        "GLI",
                        "Sport 1.6",
                        "Limited 1.6",
                        "كروس هايبرد ستاندرد",
                        "كروس هايبرد نص فل",
                        "كروس هايبرد فل كامل",
                        "GLS",
                        "ستاندرد",
                        "فل كامل",
                        "نص فل",
                        "فل كامل",
                        "بريميوم",
                        "ليميتد",
                        "ميد",
                    ]
                ],
                [request.POST["modelYear"],"select",True,[
                        "2024",
                        "2023",
                        "2022",
                        "2021",
                        "2020",
                        "2019",
                        "2018",
                        "2017",
                        "2016",
                        "2015",
                        "2014",
                        "2013",
                        "2012",
                        "2011",
                        "2010",
                        "2009",
                        "2008",
                        "2007",
                        "2006",
                        "2005",
                        "2004",
                        "2003",
                        "2002",
                        "2001",
                        "2000",
                    ]
                ],
                [request.POST["maintenance"],"select",True,[
                        "داخل الوكالة",
                        "خارج الوكالة",
                    ]
                ],
                [request.POST["status"],"select",True,[
                        "جديدة",
                        "صدمات خفيفة",
                        "صدمات قوية",
                    ]
                ],
                [request.POST["walkway"],"select",True,[
                        '10000',
                        '50000',
                        '100000',
                        '150000',
                        '200000',
                        '300000',
                        '400000',
                    ]
                ],
                [request.POST["interior"],"select",True,[
                        "جديدة",
                        "شبة جديدة",
                        "متوسطة",
                        "قديمة",
                    ]
                ],
            ]
        )

        if a == "work":
            if not mobileValidation(request.POST["phoneNumber"]):
                a = "no"
                errtitle = "يُرجى التأكد من صحة رقم الهاتف وإعادة المحاولة"

        if a == "work":
            brands={
                "تويوتا":{
                    "كامري":{
                        "GL":90000,
                        "GL Limited":112000,
                        "GL Standarnd":99820,
                        "GLX":102000,
                        "GLX Premium":107000,
                        "GLX Sport Z":120000,
                        "ستاندرد":95000,
                        "جراندي":150000,
                    },
                    "كورولا":{
                        "XLI":68400,
                        "GLI":109940,
                        "Sport 1.6":68400,
                        "Limited 1.6":109940,
                        "كروس هايبرد ستاندرد":109940,
                        "كروس هايبرد نص فل":109940,
                        "كروس هايبرد فل كامل":109940,
                    },
                },
                "هونداي":{
                    "إكسنت":{
                        "GL":40000,
                        "GLS":43000,
                        "ستاندرد":67000,
                        "فل كامل":76000,
                        "نص فل":65000,
                    },
                    "إلنترا":{
                        "فل كامل":90000,
                        "ستاندرد":70000,
                        "نص فل":80000,
                        "بريميوم":105000,
                        "ليميتد":78000,
                        "ميد":90000,
                    },
                },
            }

            car = brands[request.POST["brand"]][request.POST["vehicleType"]][request.POST["model"]]

            model_year={
                2024:1,
                2023:.95,
                2022:.9,
                2021:.85,
                2020:.8,
                2019:.75,
                2018:.7,
                2017:.65,
                2016:.6,
                2015:.55,
                2014:.5,
                2013:.45,
                2012:.4,
                2011:.35,
                2010:.3,
                2009:.25,
                2008:.2,
                2007:.15,
                2006:.14,
                2005:.13,
                2004:.12,
                2003:.11,
                2002:.1,
                2001:.09,
                2000:.08,
            }

            car = car*model_year[int(request.POST["modelYear"])]

            maintenance = {
                "داخل الوكالة":1,
                "خارج الوكالة":.95
            }
            car = car*maintenance[request.POST["maintenance"]]

            status = {
                "جديدة":1,
                "صدمات خفيفة":.95,
                "صدمات قوية":.5,
            }
            car = car*status[request.POST["status"]]

            walkway = {
                10000:.95,
                50000:.9,
                100000:.85,
                150000:.7,
                200000:.5,
                300000:.4,
                400000:.3,
            }
            car = car*walkway[int(request.POST["walkway"])]

            vehicle_interior = {
                "جديدة":1,
                "شبه جديدة":.95,
                "متوسطة":.9,
                "قديمة":.7,
            }
            car = car*vehicle_interior[request.POST["interior"]]
            product.car_seller = request.user
            product.car_name = request.POST["title"]
            product.car_description = request.POST["description"]
            product.car_brand = request.POST["brand"]
            product.car_type = request.POST["vehicleType"]
            product.car_model = request.POST["model"]
            product.car_model_year = request.POST["modelYear"]
            product.car_maintenance = request.POST["maintenance"]
            product.car_status = request.POST["status"]
            product.car_walkway = request.POST["walkway"]
            product.car_interior = request.POST["interior"]
            product.phone_number = request.POST["phoneNumber"]
            product.car_price = car
            product.save()
            deletedImages = request.POST["deletedImages"].split()
            for deleted in deletedImages:
                carImage = CarImage.objects.get(pk=int(deleted))
                carImage.delete()
            for f in request.FILES:
                createImage = CarImage.objects.create(
                    car_id = product,
                    car_image = request.FILES[f]
                )
                createImage.save()
        return JsonResponse({'errtitle':errtitle})
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)
        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
    return render(request, "edit-product.html", context)

def product(request,product_id):
    try:
        product = Car.objects.get(pk=product_id)
        car_image = CarImage.objects.filter(car_id=product)
        car_images = []
        c = 0
        for image in car_image:
            car_images.append([c, image])
            c += 1
        isFavorite = Favorite.objects.filter(favorite_product=product)
        if isFavorite:
            isFavorite = True
        else:
            isFavorite = False
    except:
        return redirect('/')
    if "delete" in request.GET:
        if product.car_seller.email == request.user.email:
            product.delete()
    if "favorite" in request.GET:
        product = Car.objects.get(pk = int(request.GET["favorite"]))
        favorite_filter = Favorite.objects.filter(favorite_product = product.pk)
        if len(favorite_filter) != 0:
            favorite_filter = Favorite.objects.get(favorite_product = product.pk)
            favorite_filter.delete()
        else:
            favorite_create = Favorite.objects.create(
                favorite_product = product,
                favorite_user = request.user
            )
            favorite_create.save()
    context = {
        "is_authenticated": request.user.is_authenticated,
        "product":product,
        "user":request.user,
        "car_images":car_images,
        "car_images_count":len(car_images),
        "isFavorite":isFavorite
    }
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
    return render(request, "product.html", context)