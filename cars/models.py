from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from collections import Counter
from .choices import brands, tags, tiers, colors, wheel_sizes, countries, months, days, years
from .validators import nickname_validator, phone_validator, validate_password_rules, name_validator, email_validator


class NewUser(models.Model):
            
    user_country_choices = countries
    user_month_choices = months
    user_day_choices = days
    user_year_choices = years

    user_nickname = models.CharField(max_length=15, unique=True, null=True, blank=True, validators=[nickname_validator], help_text="5-15 characters. Only letters and numbers. No special characters.")
    user_password = models.CharField(max_length=10, validators=[validate_password_rules], help_text="6-10 characters. Must include 1 number, 1 special character, and no character repeated more than 2 times.")
    user_name = models.CharField(max_length=255, unique=True, validators=[name_validator], help_text="Enter your full name. No numbers or special characters.")
    user_email = models.EmailField(unique=True, validators=[email_validator], help_text="Required. Must be a valid email like: example@domain.com")
    user_phone = models.CharField(max_length=15, validators=[phone_validator], null=True, blank=True, help_text="Format: +55011000000000")
    user_age_month = models.CharField(max_length=12, choices=user_month_choices, default='January', help_text="month")
    user_age_day = models.CharField(max_length=12, choices=user_day_choices, default='01', help_text="day")
    user_age_year = models.CharField(max_length=12, choices=user_year_choices, default='2025', help_text="year")
    user_country = models.CharField(max_length=50, choices=user_country_choices, help_text="Select your country of origin")
    reset_token = models.CharField(max_length=64, blank=True)
    
    def save(self, *args, **kwargs):
        if self.user_name:
            self.user_name = ' '.join([w.capitalize() for w in self.user_name.strip().split()])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name

class Cars(models.Model):

    brand_choices = brands

    car_name = models.CharField(max_length=50)
    car_version = models.CharField(max_length=50)
    car_year = models.CharField(max_length=4)
    car_brand = models.CharField(max_length=15, choices=brand_choices) 
    car_photo = models.ImageField(upload_to='photos')

    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.car_name
    
class Tags(models.Model):

    tags_choices = tags
    tags_choices_save = models.CharField(max_length=20, choices=tags_choices)

    def __str__(self):
        return self.tags_choices_save
    
class Tier(models.Model):

    tiers_choices = tiers
    tiers_choices_save = models.CharField(max_length=10, choices=tiers_choices)

    def __str__(self):
        return self.tiers_choices_save
    
class Color(models.Model):

    color_choices = colors
    color_choices_save = models.CharField(max_length=100, choices=color_choices)

    def __str__(self):
        return self.color_choices_save
    
class WheelSize(models.Model):

    wheel_size_choices = wheel_sizes
    wheel_size_choices_save = models.CharField(max_length=10, choices=wheel_size_choices)

    def __str__(self):
        return self.wheel_size_choices_save
    
class Country(models.Model):

    country_choices = countries
    country_choices_save = models.CharField(max_length=50, choices=country_choices)

    def __str__(self):
        return self.country_choices_save

class Cardata(models.Model):
    car_name_data = Cars.car_name
    tiers_cars_choices = Tier.tiers_choices
    tags_cars_choices = Tags.tags_choices
    color_cars_choices = Color.color_choices
    wheel_size_cars_choices = WheelSize.wheel_size_choices
    country_cars_choices = Country.country_choices
    car_tier = models.CharField(max_length=10, choices=tiers_cars_choices, null=True, blank=True) 
    car_tag = models.CharField(max_length=20, choices=tags_cars_choices, null=True, blank=True)
    car_power = models.CharField(max_length=5, null=True)
    car_torque = models.CharField(max_length=5, null=True)
    car_color = models.CharField(max_length=100, choices=color_cars_choices, null=True, blank=True)
    car_wheel_size_front = models.CharField(max_length=100, choices=wheel_size_cars_choices, null=True, blank=True)
    car_wheel_size_back = models.CharField(max_length=100, choices=wheel_size_cars_choices, null=True, blank=True)
    car_country = models.CharField(max_length=100, choices=country_cars_choices, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    car_file = models.FileField(upload_to="car_file", null=True)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car.car_name