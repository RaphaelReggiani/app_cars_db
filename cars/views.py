from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Cars, Tags, Cardata, Tier, Color, WheelSize, Country, NewUser
from django.contrib import messages
from django.contrib.messages import constants, get_messages
from django.db.models import Q
from django.core.exceptions import ValidationError
import re
from collections import Counter
from django.contrib.auth.models import User
import datetime
from .forms import SignUpForm, LoginForm, FinalizeUserForm, UserEditForm
from django.contrib.auth.hashers import make_password, check_password



def home(request):
    return render(request, 'home.html')

def user_auth(request):

    signup_form = SignUpForm(prefix='signup')
    login_form = LoginForm(prefix='login')
    return render(request, 'user.html', {
        'signup_form': signup_form,
        'login_form': login_form,
        'user_countries': NewUser.user_country_choices,
        'user_months': NewUser.user_month_choices,
        'user_days': NewUser.user_day_choices,
        'user_years': NewUser.user_year_choices
    })

def user_pre_register(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            cleaned_data = signup_form.cleaned_data

            request.session['pre_user_data'] = {
                'user_name': cleaned_data['user_name'],
                'user_email': cleaned_data['user_email'],
                'user_phone': cleaned_data['user_phone'],
                'user_country': cleaned_data['user_country'],
                'user_age_month': cleaned_data['user_age_month'],
                'user_age_day': cleaned_data['user_age_day'],
                'user_age_year': cleaned_data['user_age_year'],
            }

            return redirect('user_finalize_register')
        else:
            messages.error(request, 'Please correct the errors below.')
            login_form = LoginForm(prefix='login')
            return render(request, 'user.html', {
                'signup_form': signup_form,
                'login_form': login_form,
                'user_countries': NewUser.user_country_choices,
                'user_months': NewUser.user_month_choices,
                'user_days': NewUser.user_day_choices,
                'user_years': NewUser.user_year_choices
            })
    return redirect('user')


def user_finalize_register(request):
    pre_user_data = request.session.get('pre_user_data')
    if not pre_user_data:
        messages.error(request, "Please complete the first step before finalizing registration.")
        return redirect('user')
    
    success = False

    if request.method == 'POST':
        form = FinalizeUserForm(request.POST)
        if form.is_valid():
            user_nickname = form.cleaned_data['user_nickname']

            if NewUser.objects.filter(user_nickname=user_nickname).exists():
                messages.error(request, 'Nickname already taken. Please choose another one.')
            else:

                user = NewUser(
                    user_name=pre_user_data['user_name'],
                    user_email=pre_user_data['user_email'],
                    user_phone=pre_user_data['user_phone'],
                    user_country=pre_user_data['user_country'],
                    user_age_month=pre_user_data['user_age_month'],
                    user_age_day=pre_user_data['user_age_day'],
                    user_age_year=pre_user_data['user_age_year'],
                    user_nickname=user_nickname,
                    user_password=make_password(form.cleaned_data['user_password']),
                )
                user.save()

                del request.session['pre_user_data']

                messages.success(request, 'User registered successfully!')
                success = True
        else:
            messages.error(request, 'Username already exists, insert another one.')
    else:
        form = FinalizeUserForm()

    return render(request, 'user_register.html', {'form': form, 'success': success})

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import NewUser

def user_login(request):
    if request.method == 'POST':
        user_nickname = request.POST.get('user_nickname')
        user_password = request.POST.get('user_password')

        try:
            user = NewUser.objects.get(user_nickname=user_nickname)
            if check_password(user_password, user.user_password):

                request.session['user_id'] = user.id
                request.session['user_nickname'] = user.user_nickname

                messages.success(request, f'Welcome back, {user.user_nickname}!', extra_tags='login')
                return redirect('home')
            else:
                messages.error(request, 'Incorrect password.', extra_tags='login')
        except NewUser.DoesNotExist:
            messages.error(request, 'User not found.', extra_tags='login')

    signup_form = SignUpForm(prefix='signup')
    login_form = LoginForm(prefix='login')
    return render(request, 'user.html', {
        'signup_form': signup_form,
        'login_form': login_form,
        'user_countries': NewUser.user_country_choices,
        'user_months': NewUser.user_month_choices,
        'user_days': NewUser.user_day_choices,
        'user_years': NewUser.user_year_choices
    })

def user_logout(request):

    request.session.flush()
    storage = get_messages(request)

    for _ in storage:
        pass

    return redirect('home')


def user_informations(request, user_id):
    session_user_id = request.session.get('user_id')
    if not session_user_id:
        messages.error(request, "You must be logged in to access this page.")
        return redirect("user_login")

    if int(session_user_id) != int(user_id):
        messages.error(request, "You cannot access another user's profile.")
        return redirect("home")

    try:
        user = NewUser.objects.get(id=session_user_id)
    except NewUser.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect("home")

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your informations were updated successfully!")
            return redirect('user_informations', user_id=user.id)
        else:
            messages.error(request, "There was an error in the form.")
    else:
        form = UserEditForm(instance=user)

    return render(request, 'user_informations.html', {
        'user': user,
        'form': form,
        'user_months': NewUser.user_month_choices,
        'user_days': NewUser.user_day_choices,
        'user_years': NewUser.user_year_choices,
        'user_countries': NewUser.user_country_choices,
    })


def cars(request):

    if request.method == "GET":
        cars = Cars.objects.all()
        show_cars = Cars.objects.order_by('-id')[:4]
        return render(request, 'new_car.html', {
            'car_brands': Cars.brand_choices, 
            'cars': cars, 
            'show_cars' : show_cars,
        })
    
    elif request.method == "POST":
        car_name = request.POST.get('car_name')
        car_version = request.POST.get('car_version')
        car_year = request.POST.get('car_year')
        car_brand = request.POST.get('car_brand')
        car_photo = request.FILES.get('car_photo')

        user_id = request.session.get('user_id')
        if not user_id:
            messages.error(request, 'You must be logged in to register a car.')
            return redirect('cars')

        try:
            user = NewUser.objects.get(id=user_id)
        except NewUser.DoesNotExist:
            messages.error(request, 'User not found. Please log in again.')
            return redirect('cars')

        if len(car_name.strip()) == 0 or len(car_version.strip()) == 0 or len(car_year.strip()) == 0 or not car_photo:
            messages.add_message(request, constants.ERROR, 'All the fields needs to be filled.')
            return redirect('cars')

        car = Cars(
                
            car_name=car_name,
            car_version=car_version,
            car_year=car_year,
            car_brand=car_brand,
            car_photo=car_photo,
            user=user,
        )

        car.save()
            
        messages.add_message(request, constants.SUCCESS, 'Registration completed successfully.')
            
        return redirect('cars')

def car_view(request, id):
    car = Cars.objects.get(id=id)
    car_data = Cardata.objects.filter(car=car).last()
    if request.method == "GET":
        return render(request, 'car.html', {
            'car' : car, 
            'car_data': car_data, 
            'tags_choices' : Tags.tags_choices, 
            'tiers_choices' : Tier.tiers_choices, 
            'color_choices' : Color.color_choices, 
            'wheel_size_choices_front' : WheelSize.wheel_size_choices, 
            'wheel_size_choices_back' : WheelSize.wheel_size_choices, 
            'country_choices' : Country.country_choices,
        })
    
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
    
    return render(request, 'show_car.html', {
        'car_shown_main' : car_shown_main, 
        'car_shown_description' : car_shown_description,
    })

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
        return render(request, 'car_main_edit.html', {
            'car_brands': Cars.brand_choices, 
            'car': car,
        })

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

