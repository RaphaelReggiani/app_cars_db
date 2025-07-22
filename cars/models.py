from django.db import models

class Cars(models.Model):

    brand_choices = (
        ('Ferrari', 'Ferrari'),
        ('Lamborghini', 'Lamborghini'),
        ('koenigsegg', 'koenigsegg'),
        ('Bugatti', 'Bugatti'),
        ('McLaren', 'McLaren'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('Bentley', 'Bentley'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Audi', 'Audi'),
        ('Dodge', 'Dodge'),
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Tesla', 'Tesla'),
        ('BYD', 'BYD'),
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
        ('SUV', 'SUV'),
        ('PICKUP', 'PICKUP'),
        ('EV', 'EV'),
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
    
class Color(models.Model):
    color_choices = (
        ('White', 'White'),
        ('Black', 'Black'),
        ('Silver', 'Silver'),
        ('Red', 'Red'),
        ('Light Blue', 'Light Blue'),
        ('Blue', 'Blue'),
        ('Navy Blue', 'Navy Blue'),
        ('Purple', 'Purple'),
        ('Pink', 'Pink'),
        ('Violet', 'Violet'),
        ('Orange', 'Orange'),
        ('Green', 'Green'),
        ('Gray', 'Gray'),
        ('Gold', 'Gold'),
        ('Wrapped', 'Wrapped'),
        ('Exposed Carbon Fiber', 'Exposed Carbon Fiber'),
        ('Others', 'Others'),
    )
    color_choices_save = models.CharField(max_length=100, choices=color_choices)

    def __str__(self):
        return self.color_choices_save
    
class WheelSize(models.Model):
    wheel_size_choices = (
        ('15"', '15"'),
        ('16"', '16"'),
        ('17"', '17"'),
        ('18"', '18"'),
        ('19"', '19"'),
        ('20"', '20"'),
        ('21"', '21"'),
        ('22"', '22"'),
        ('23"', '23"'),
        ('24"', '24"'),
        ('25"', '25"'),
        ('26"', '26"'),
        ('27"', '27"'),
        ('28"', '28"'),
        ('29"', '29"'),
        ('30"', '30"'),
        ('Others', 'Others'),
    )
    wheel_size_choices_save = models.CharField(max_length=10, choices=wheel_size_choices)

    def __str__(self):
        return self.wheel_size_choices_save
    
class Country(models.Model):
    country_choices = (
        ('USA', 'USA'),
        ('Brazil', 'Brazil'),
        ('Canada', 'Canada'),
        ('UK', 'UK'),
        ('France', 'France'),
        ('Italy', 'Italy'),
        ('Germany', 'Germany'),
        ('Japan', 'Japan'),
        ('China', 'China'),
        ('Australia', 'Australia'),
        ('Others', 'Others'),
    )
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