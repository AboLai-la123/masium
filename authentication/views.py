from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from home.models import formChecker
from django.contrib.auth import authenticate
from django.contrib import auth
import re
 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validateEmail(email):
    print("asd")
    if(re.fullmatch(regex, email)):
        return False
    else:
        return True

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        a, errtitle = formChecker([
                [request.POST["email"],75,True,[
                        "يرجى ملئ جميع الحقول",
                        "الحد الأقصى للأحرف في البريد الإلكتروني هو 75 حرفًا"
                    ]
                ],
                [request.POST["password"],50,True,[
                        "يرجى ملئ جميع الحقول",
                        "الحد الأقصى للأحرف في كلمة المرور هو 50 حرفًا"
                    ]
                ]
            ]
        )
        if a == "work":
            emailFilter = User.objects.filter(email = request.POST["email"])
            if len(emailFilter) == 0:
                a = "no"
                errtitle = "البريد الإلكتروني غير صحيح"
            else:
                emailGet = User.objects.get(email = request.POST["email"])
        if a == "work":
            user = authenticate(username = emailGet.username,password = request.POST["password"])
            if user is None:
                a = "no"
                errtitle = "كلمة المرور غير صحيحة"
        if a == "work":
            auth.login(request,user)
        return JsonResponse({'errtitle':errtitle})
    context = {}
    return render(request, "login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("/authentication/login")

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
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
                [request.POST["password"],50,True,[
                        "يرجى ملئ جميع الحقول",
                        "الحد الأقصى للأحرف في كلمة المرور هو 50 حرفًا"
                    ]
                ]
            ]
        )
        if a == "work":
            emailFilter = User.objects.filter(email = request.POST["email"])
            if len(emailFilter) != 0:
                a = "no"
                errtitle = "البريد الإلكتروني مستخدم مسبقاً"
            elif validateEmail(request.POST["email"]):
                a = "no"
                errtitle = "البريد الإلكتروني غير صحيح"
        if a == "work":
            password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
            
            if not re.match(password_pattern, request.POST["password"]):
                a = "no"
                errtitle = "كلمة المرور ضعيفة"
        if a == "work":
            user_create = User.objects.create_user(
                username = request.POST["email"],
                email = request.POST["email"],
                password = request.POST["password"],
                first_name = request.POST["firstName"],
                last_name = request.POST["lastName"],
            )
            user_create.save()
            auth.login(request,user_create)
        return JsonResponse({'errtitle':errtitle})
    context = {}
    return render(request, "signup.html", context)