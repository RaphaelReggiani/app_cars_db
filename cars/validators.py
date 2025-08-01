from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from collections import Counter


def validate_password_rules(value):
    if not (6 <= len(value) <= 10):
        raise ValidationError("Password must be between 6 and 10 characters long.")

    if not re.search(r'\d', value):
        raise ValidationError("Password must contain at least one number.")

    if not re.search(r'[!@#$%^&*()_\-+=\[\]{};:,.<>?/\\|`~]', value):
        raise ValidationError("Password must contain at least one special character.")

    counter = Counter(value)
    for char, count in counter.items():
        if count > 2:
            raise ValidationError(f"Character '{char}' is repeated more than twice.")
        
def name_validator(value):
    if not value or value.strip() == "":
        raise ValidationError("Name cannot be empty.")

    words = value.strip().split()

    if len(words) < 2:
        raise ValidationError("Name must include at least first and last name.")

    for word in words:
        if len(word) < 3:
            raise ValidationError("Each part of the name must be at least 3 characters long.")
        if not word.isalpha():
            raise ValidationError("Name must only contain alphabetic characters (no numbers or special characters).")

def email_validator(value):
    if not value or value.strip() == "":
        raise ValidationError("Email cannot be empty.")

    if "@" not in value:
        raise ValidationError("Email must contain '@' symbol.")

    local_part = value.split("@")[0]

    if not local_part:
        raise ValidationError("Email must have a local part before '@'.")

    if " " in value:
        raise ValidationError("Email cannot contain spaces.")

    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
        raise ValidationError("Enter a valid email address.")

nickname_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9]{5,15}$',
    message="Nickname must be 5-15 characters long and contain only letters and numbers."
)

phone_validator = RegexValidator(regex=r'^\+55\d{12}$',message="Phone number must be in the format: +55011000000000")

