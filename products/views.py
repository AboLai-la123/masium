from django.shortcuts import render, redirect
from django.http import JsonResponse
from home.models import *
from .models import *
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
            vehicleTypes.append('أفالون')
            vehicleTypes.append('يارس')
            vehicleTypes.append('هايلاندر')
            vehicleTypes.append('فروتشنر')
            vehicleTypes.append('لاندكروزر')
            vehicleTypes.append('برادو')
        elif product.car_brand == "هونداي":
            vehicleTypes.append('إكسنت')
            vehicleTypes.append('إلنترا')
            vehicleTypes.append('سوناتا')
            vehicleTypes.append('أزيرا')
            vehicleTypes.append('كريتا')
            vehicleTypes.append('سنتافي')
        elif product.car_brand == "جمس":
            vehicleTypes.append('سييرا')
            vehicleTypes.append('يوكن')
            vehicleTypes.append('يوكن XL')
            vehicleTypes.append('أكاديا')
        elif product.car_brand == "فورد":
            vehicleTypes.append('F150')
            vehicleTypes.append('إكسبلورر')
            vehicleTypes.append('إكسبديشن')
            vehicleTypes.append('إيدج')
            vehicleTypes.append('توروس')
            vehicleTypes.append('فليكس')
            vehicleTypes.append('كراون فكتوريا')
        
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
        elif product.car_type == "أفالون":
            models.append("ليميتد")
            models.append("بريميوم")
            models.append("ستاندرد")
            models.append("XL")
            models.append("SE")
        elif product.car_type == "يارس":
            models.append("S")
            models.append("STD")
            models.append("Y")
            models.append("E")
            models.append("SE")
        elif product.car_type == "هايلاندر":
            models.append("هايبرد")
            models.append("ليميتد")
            models.append("VXR")
            models.append("GXR")
        elif product.car_type == "فورتشنر":
            models.append("GX")
            models.append("VX")
            models.append("TRD")
        elif product.car_type == "لاندكروزر":
            models.append("GXR")
            models.append("VXR")
            models.append("VXS")
            models.append("GR")
            models.append("VX")
        elif product.car_type == "برادو":
            models.append("TX")
            models.append("TXL")
            models.append("VX")
            models.append("VXR")
        elif product.car_type == "سوناتا":
            models.append("GDI")
            models.append("GL")
            models.append("GLS")
            models.append("ستاندرد")
            models.append("فل كامل")
            models.append("نص فل")
        elif product.car_type == "أزيرا":
            models.append("فل كامل")
            models.append("ستاندرد")
            models.append("نص فل")
            models.append("بريميوم")
            models.append("كلاسيك")
        elif product.car_type == "كريتا":
            models.append("GL")
            models.append("GLS")
            models.append("فل كامل")
            models.append("نص فل")
            models.append("ستاندرد")
        elif product.car_type == "سنتافي":
            models.append("GL")
            models.append("GLS")
            models.append("نص فل")
            models.append("ستاندرد")
            models.append("فل كامل")
        elif product.car_type == "سييرا":
            models.append("SLE")
            models.append("ستاندرد")
            models.append("دينالي")
            models.append("SLT")
            models.append("AT4")
        elif product.car_type == "يوكن":
            models.append("SLE")
            models.append("SLT")
            models.append("دينالي")
            models.append("AT4")
        elif product.car_type == "يوكن XL":
            models.append("SLE")
            models.append("SLT")
            models.append("دينالي")
        elif product.car_type == "أكاديا":
            models.append("SLE")
            models.append("SLT")
            models.append("دينالي")
            models.append("AT4")
        elif product.car_type == "F150":
            models.append("Lariat")
            models.append("Raptor")
            models.append("XLT")
            models.append("بلاتينوم")
            models.append("سبيشال اديشن")
        elif product.car_type == "إكسبلورر":
            models.append("XLT")
            models.append("سبورت")
            models.append("ستاندرد")
            models.append("ليميتد")
            models.append("نص فل")
            models.append("بلاتينوم")
        elif product.car_type == "إكسبديشن":
            models.append("XL")
            models.append("XLT")
            models.append("ستاندرد")
            models.append("ليميتد دبل")
            models.append("بلاتينيوم")
        elif product.car_type == "إيدج":
            models.append("SEL")
            models.append("SE")
            models.append("تيتانيوم")
            models.append("ليميتد")
            models.append("ستاندرد")
        elif product.car_type == "توروس":
            models.append("SE")
            models.append("SEL")
            models.append("ليميتد")
            models.append("ستاندرد")
            models.append("فل كامل")
            models.append("ايكوبوست")
        elif product.car_type == "فليكس":
            models.append("SEL")
            models.append("ستاندرد")
            models.append("ليميتد")
        elif product.car_type == "كراون فكتوريا":
            models.append("فل كامل")
            models.append("نص فل")
            models.append("بوليسي")
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
                        "جمس",
                        "فورد",
                    ]
                ],
                [request.POST["vehicleType"],"select",True,[
                        "كامري",
                        "أفالون",
                        "يارس",
                        "هايلاندر",
                        "فورتشنر",
                        "لاندكروزر",
                        "برادو",
                        "كورولا",
                        "إكسنت",
                        "سوناتا",
                        "أزيرا",
                        "كريتا",
                        "سنتافي",
                        "إلنترا",
                        "سييرا",
                        "يوكن",
                        "يوكن XL",
                        "أكاديا",
                        "F150",
                        "إكسبلورر",
                        "إكسبديشن",
                        "إيدج",
                        "توروس",
                        "فليكس",
                        "كراون فيكتوريا",
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

                    "أفالون":{
                        "ليميتد":163000,
                        "بريميوم":180000,
                        "ستاندرد":150000,
                        "XL":114000,
                        "SE":143000,
                    },
                    "يارس":{
                        "S":53000,
                        "STD":60000,
                        "Y":60000,
                        "E":53300,
                        "SE":46000,
                    },
                    "هايلاندر":{
                        "هايبرد":160000,
                        "ليميتد":193000,
                        "VXR":200000,
                        "GXR":172000,
                    },
                    "فورتشنر":{
                        "GX":135000,
                        "VX":151000,
                        "TRD":113000,
                    },
                    "لاندكروزر":{
                        "GXR":286000,
                        "VXR":304000,
                        "VXS":330000,
                        "GR":400000,
                        "VX":350000,
                    },
                    "برادو":{
                        "TX":145000,
                        "TXL":176000,
                        "VX":200000,
                        "VXR":202000,
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
                    "سوناتا":{
                        "GDI":106000,
                        "GL":75000,
                        "GLS":90000,
                        "ستاندرد":97000,
                        "فل كامل":112000,
                        "نص فل":100000,
                    },
                    "أزيرا":{
                        "فل كامل":115000,
                        "ستاندرد":85000,
                        "نص فل":100000,
                        "بريميوم":170000,
                        "كلاسيك":150000,
                    },
                    "كريتا":{
                        "GL":60000,
                        "GLS":65000,
                        "فل كامل":76000,
                        "نص فل":89000,
                        "ستاندرد":65000,
                    },
                    "سنتافي":{
                        "GL":77000,
                        "GLS":90000,
                        "نص فل":100000,
                        "ستاندرد":100000,
                        "فل كامل":112000,
                    },
                },
                "جمس":{
                    "سييرا":{
                        "SLE":184000,
                        "ستاندرد":133000,
                        "دينالي":290000,
                        "SLT":250000,
                        "AT4":225000,
                    },
                    "يوكن":{
                        "SLE":240000,
                        "SLT":280000,
                        "دينالي":335000,
                        "AT4":300000,
                    },
                    "يوكن XL":{
                        "SLE":240000,
                        "SLT":300000,
                        "دينالي":290000,
                    },
                    "أكاديا":{
                        "SLE":133000,
                        "SLT":180000,
                        "دينالي":200000,
                        "AT4":165000,
                    }
                },
                "فورد":{
                    "F150":{
                        "Lariat":193000,
                        "Raptor":300000,
                        "XLT":260000,
                        "بلاتينوم":280000,
                        "سبيشال اديشن":193000,
                    },
                    "إكسبلورر":{
                        "XLT":135000,
                        "سبورت":200000,
                        "ستاندرد":150000,
                        "ليميتد":200000,
                        "نص فل":175000,
                        "بلاتينوم":241000,
                    },
                    "إكسبديشن":{
                        "XL":150000,
                        "XLT":240000,
                        "ستاندرد":158000,
                        "ليميتد دبل":294000,
                        "بلاتينيوم":293000,
                    },
                    "إيدج":{
                        "SEL":166000,
                        "SE":120000,
                        "تيتانيوم":180000,
                        "ليميتد":120000,
                        "ستاندرد":133000,
                    },
                    "توروس":{
                        "SE":112000,
                        "SEL":130000,
                        "ليميتد":158000,
                        "ستاندرد":125000,
                        "فل كامل":150000,
                        "ايكوبوست":100000,
                    },
                    "فليكس":{
                        "SEL":120000,
                        "ستاندرد":144000,
                        "ليميتد":111000,
                    },
                    "كراون فكتوريا":{
                        "فل كامل":77000,
                        "نص فل":70000,
                        "بوليسي":92000,
                    }
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
            if request.user.email != product.car_seller.email:
                notificationCreate = Notification.objects.create(
                    notification_user = product.car_seller,
                    notification_title = "تعليق جديد",
                    notification_description = f"تعليق جديد بخصوص المركبة '{product.car_name[0:20]}'",
                    notification_link = f"/products/{product.pk}",
                )
                notificationCreate.save()
            rateCreate = ProductRating.objects.create(
                rate_sender = request.user,
                rate_product = product,
                rate_content = request.POST["content"]
            )
        
        return JsonResponse({"errtitle":errtitle})
    
    ratings = ProductRating.objects.filter(rate_product = product)[::-1]
    context = {
        "is_authenticated": request.user.is_authenticated,
        "product":product,
        "user":request.user,
        "car_images":car_images,
        "car_images_count":len(car_images),
        "isFavorite":isFavorite,
        "ratings":ratings
    }
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(favorite_user=request.user)
        favoriteCount = len(favorites)

        notification = Notification.objects.filter(notification_user=request.user,notification_is_new=True)
        notificationCount = len(notification)
        context["favoriteCount"] = favoriteCount
        context["notificationCount"] = notificationCount
    return render(request, "product.html", context)