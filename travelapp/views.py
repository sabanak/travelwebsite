from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import new


def fun(request):
    obj=place.objects.all()
    objj = new.objects.all().order_by('-blog_date')
    return render(request,"index.html",{'results':obj,'res':objj})


#STATIC PAGE
# def fun(request):
#     obj=place()
#     obj.name="kerala"
#     obj.price="100"
#     obj.desc="this is kerala"
#     objj = news()
#     objj.date_time = 2
#     objj.date_ti = "June"
#     objj.heading = "journey"
#     objj.sub = "happy journey"
#     objj.details = "every journey"
#     return render(request,"index.html",{'results':obj,'res':objj})


# def addition(request):
#     num1=int(request.POST["num1"])
#     num2=int(request.POST["num2"])
#     num3=num1+num2
#     return render(request,"result.html",{'add':num3})
