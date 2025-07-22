from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Cars, Tags, Cardata, Tier, Color, WheelSize, Country
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Q
import datetime


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
    car_data = Cardata.objects.filter(car=car).last()
    if request.method == "GET":
        tags_car_information = Tags.objects.all()
        tiers_car_information = Tier.objects.all()
        color_car_information = Color.objects.all()
        wheel_size_car_information = WheelSize.objects.all()
        country_car_information = Country.objects.all()
        return render(request, 'car.html', {'car' : car, 'car_data': car_data, 'tags_choices' : Tags.tags_choices, 'tiers_choices' : Tier.tiers_choices, 'color_choices' : Color.color_choices, 'wheel_size_choices_front' : WheelSize.wheel_size_choices, 'wheel_size_choices_back' : WheelSize.wheel_size_choices, 'country_choices' : Country.country_choices})
    
    elif request.method == "POST":
        car_tier = request.POST.get('car_tier')
        car_tag = request.POST.get('car_tag')
        car_power = request.POST.get('car_power')
        car_torque = request.POST.get('car_torque')
        car_color = request.POST.get('car_color')
        car_wheel_size_front = request.POST.get('car_wheel_size_front')
        car_wheel_size_back = request.POST.get('car_wheel_size_back')
        car_country = request.POST.get('car_country')
        description = request.POST.get('description')
        car_file = request.FILES.get('car_file')
        
        
        car_data = Cardata(
            car_tier = car_tier,
            car_tag = car_tag,
            car_power = car_power,
            car_torque = car_torque,
            car_color = car_color,
            car_wheel_size_front = car_wheel_size_front,
            car_wheel_size_back = car_wheel_size_back,
            car_country = car_country,
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

import datetime

def all_cars(request):
    query = request.GET.get('q', '')
    brand = request.GET.get('brand', '')
    year = request.GET.get('year', '')
    color = request.GET.get('color', '')
    type_filter = request.GET.get('type', '')

    brand_choices = Cars.brand_choices
    color_choices = Color.color_choices
    tag_choices = Tags.tags_choices

    import datetime
    current_year = datetime.datetime.now().year
    years = ['Before 1990'] + [str(y) for y in range(1990, current_year + 1)]

    car_ids_from_cardata = Cardata.objects.all()
    if color:
        car_ids_from_cardata = car_ids_from_cardata.filter(car_color__icontains=color)
    if type_filter:
        car_ids_from_cardata = car_ids_from_cardata.filter(car_tag__icontains=type_filter)

    car_ids_from_cardata = car_ids_from_cardata.values_list('car_id', flat=True)

    cars = Cars.objects.all()

    if query:
        cars = cars.filter(
            Q(car_name__icontains=query) |
            Q(car_brand__icontains=query) |
            Q(car_year__icontains=query)
        )

    if brand:
        cars = cars.filter(car_brand=brand)

    if year:
        if year == 'Before 1990':
            cars = cars.filter(car_year__lt='1990')
        else:
            cars = cars.filter(car_year=year)

    if color or type_filter:
        cars = cars.filter(id__in=car_ids_from_cardata)

    cars = cars.distinct().order_by('-id')

    return render(request, 'all_cars.html', {
        'car_main': cars,
        'car_information': Cardata.objects.all().order_by('-id'),
        'query': query,
        'brand_choices': brand_choices,
        'color_choices': color_choices,
        'tag_choices': tag_choices,
        'years': years,
        'request': request,
    })


def car_main_edit(request, id):
    try:
        car = Cars.objects.get(id=id)
    except Cars.DoesNotExist:
        raise Http404("Car not found.")

    if request.method == "GET":
        return render(request, 'car_main_edit.html', {'car_brands': Cars.brand_choices, 'car': car})

    elif request.method == "POST":
        car_name = request.POST.get('car_name')
        car_version = request.POST.get('car_version')
        car_year = request.POST.get('car_year')
        car_brand = request.POST.get('car_brand')
        car_photo = request.FILES.get('car_photo')

        if not car_name.strip() or not car_version.strip() or not car_year.strip():
            messages.add_message(request, constants.ERROR, 'All fields must be filled.')
            return redirect('car_main_edit', id=id)

        car.car_name = car_name
        car.car_version = car_version
        car.car_year = car_year
        car.car_brand = car_brand
        if car_photo:
            car.car_photo = car_photo

        car.save()

        messages.add_message(request, constants.SUCCESS, 'Informations updated successfully.')
        return redirect('car_main_edit', id=id)

