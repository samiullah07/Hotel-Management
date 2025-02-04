from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import *
# Create your views here.

def Index(request):
    amenities = Amenities.objects.all()
    

    return render(request,"index.html",{"amenities":amenities})



def get_api(request):
    hotel_objs = Hotel.objects.all()

    if request.GET.get("sort-by"):
        sort_by =  request.GET.get("sort-by") 
        if sort_by == "asc":
          hotel_objs = hotel_objs.order_by("hotel_price")
        elif sort_by== "dsc":
            hotel_objs = hotel_objs.order_by("-hotel_price")

    if request.GET.get("price"):
      
        price = request.GET.get("price")
        hotel_objs = Hotel.objects.filter(hotel_price = price)

    payroll = []

    for obj in hotel_objs:
        payroll.append({
          "hotel_name" : obj.hotel_name,
           "hotel_description" : obj.hotel_description,
           "hotel_price" : obj.hotel_price,
           "banner_image" : str(obj.banner_img),
           "get_amenities" : obj.get_Amenities()
                        })
    

        

    return JsonResponse(payroll,safe=False)

