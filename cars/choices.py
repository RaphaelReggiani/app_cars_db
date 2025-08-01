import pycountry, datetime

months = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December')
)

days = [(str(day).zfill(2), str(day).zfill(2)) for day in range(1, 32)]

current_year = datetime.datetime.now().year
years = [(str(year), str(year)) for year in range(current_year, 1949, -1)]

brands = (
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

tags = (
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

tiers = (
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

colors = (
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

wheel_sizes = (
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

countries = sorted(
    [(country.name, country.name) for country in pycountry.countries],
    key=lambda x: x[1]
)