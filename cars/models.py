from django.db import models

class Cars(models.Model):

    brand_choices = (
        ('Ferrari', 'Ferrari'),
        ('Lamborghini', 'Lamborghini'),
        ('koenigsegg', 'koenigsegg'),
        ('Bugatti', 'Bugatti'),
        ('McLaren', 'McLaren'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Audi', 'Audi'),
        ('Dodge', 'Dodge'),
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Others', 'Others')
    )

    car_name = models.CharField(max_length=50)
    car_version = models.CharField(max_length=50)
    car_year = models.CharField(max_length=4)
    car_brand = models.CharField(max_length=15, choices=brand_choices) 
    car_photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.car_name
    
class Tags(models.Model):
    tags_choices = (
        ('HYPER CAR', 'HYPER CAR'),
        ('SUPER CAR', 'SUPER CAR'),
        ('SPORT CAR', 'SPORT CAR'),
        ('MUSCLE CAR', 'MUSCLE CAR'),
        ('LUXURY CAR', 'LUXURY CAR'),
        ('COLLECTIBLE CAR', 'COLLECTIBLE CAR'),
        ('RACE CAR', 'RACE CAR'),
        ('COMMON CAR', 'COMMON CAR'),
        ('OTHERS', 'OTHERS'),
    )
    tags_choices_save = models.CharField(max_length=20, choices=tags_choices)

    def __str__(self):
        return self.tags_choices_save
    
class Tier(models.Model):
    tiers_choices = (
        ('S+', 'S+'),
        ('S', 'S'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    tiers_choices_save = models.CharField(max_length=10, choices=tiers_choices)

    def __str__(self):
        return self.tiers_choices_save

class Cardata(models.Model):
    car_name_data = Cars.car_name
    tiers_cars_choices = Tier.tiers_choices
    tags_cars_choices = Tags.tags_choices
    car_tier = models.CharField(max_length=10, choices=tiers_cars_choices, null=True, blank=True) 
    car_tag = models.CharField(max_length=20, choices=tags_cars_choices, null=True, blank=True)
    car_power = models.CharField(max_length=5, null=True)
    car_torque = models.CharField(max_length=5, null=True)
    description = models.TextField(null=True, blank=True)
    car_file = models.FileField(upload_to="car_file", null=True)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car.car_name