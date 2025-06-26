from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Cars, Tags, Cardata, Tier
from django.contrib import messages
from django.contrib.messages import constants


def home(request):
    return render(request, 'home.html')

def cars(request):

        if request.method == "GET":
            cars = Cars.objects.all()
            show_cars = Cars.objects.order_by('-id')[:4]
            return render(request, 'new_car.html', {'car_brands': Cars.brand_choices, 'cars': cars, 'show_cars' : show_cars})
    
        elif request.method == "POST":
            car_name = request.POST.get('car_name')
            car_version = request.POST.get('car_version')
            car_year = request.POST.get('car_year')
            car_brand = request.POST.get('car_brand')
            car_photo = request.FILES.get('car_photo')

            if len(car_name.strip()) == 0 or len(car_version.strip()) == 0 or len(car_year.strip()) == 0 or not car_photo:
                messages.add_message(request, constants.ERROR, 'All the fields needs to be filled.')
                return redirect('cars')

            car = Cars(
                
                car_name=car_name,
                car_version=car_version,
                car_year=car_year,
                car_brand=car_brand,
                car_photo=car_photo
            )

            car.save()
            
            messages.add_message(request, constants.SUCCESS, 'Registration completed successfully.')
            
            return redirect('cars')

def car_view(request, id):
    car = Cars.objects.get(id=id)
    if request.method == "GET":
        tags_car_information = Tags.objects.all()
        tiers_car_information = Tier.objects.all() 
        return render(request, 'car.html', {'car' : car, 'tags_choices' : Tags.tags_choices, 'tiers_choices' : Tier.tiers_choices})
    
    elif request.method == "POST":
        car_tier = request.POST.get('car_tier')
        car_tag = request.POST.get('car_tag')
        car_power = request.POST.get('car_power')
        car_torque = request.POST.get('car_torque')
        description = request.POST.get('description')
        car_file = request.FILES.get('car_file')
        
        
        car_data = Cardata(
            car_tier = car_tier,
            car_tag = car_tag,
            car_power = car_power,
            car_torque = car_torque,
            description = description,
            car_file = car_file,
            car = car,
        )
        
        car_data.save()
        
        messages.add_message(request, constants.SUCCESS, 'Informations updated successfully.')
        return redirect(f'/cars/{id}')
     
def update_car_data(request, id):
     car = Cars.objects.get(id=id)
     car.save()
     return redirect(f'/cars/{id}')

def car_exclude(request,id):
    car = Cars.objects.get(id=id)
    car.delete()
    return redirect(f'/cars/')

def show_car(request,id):
    car_shown_main = Cars.objects.get(id=id)
    car_shown_description = Cardata.objects.filter(car=car_shown_main).last()
    
    return render(request, 'show_car.html', {'car_shown_main' : car_shown_main, 'car_shown_description' : car_shown_description})

def all_cars(request):
    car_main = Cars.objects.all()
    car_information = Cardata.objects.all()
    
    return render(request, 'all_cars.html', {'car_main' : car_main, 'car_information' : car_information})