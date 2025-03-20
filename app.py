import re

def is_valid_email(email):
    
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def rectangle_area(width, height):
   
    if width < 0 or height < 0:
        return None
    return width * height

def filter_even_numbers(numbers):
    
    return [num for num in numbers if num % 2 == 0]

def convert_date_format(date):
    
    if "-" not in date:
        raise ValueError("Invalid date format. Expected DD-MM-YYYY")
    day, month, year = date.split("-")
    return f"{year}-{month}-{day}"

def is_palindrome(text):
    
    text = text.replace(" ", "").lower()
    return text == text[::-1]
