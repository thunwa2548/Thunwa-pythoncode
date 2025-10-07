"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print("=== PERSONAL INFORMATION VALIDATOR ===")

name = input("enter your name :")
age = input("enter your age :")
phone = input("enter your phone :")


# Name Validation
nameFlag = all(char.isalpha() or char == " " for char in name)

# Age Validation
ageFlag = False
if age.isdigit():
    age = int(age)
    if 18 <= age <= 65:
        ageFlag = True
else:
    ageFlag = False

# Phone Number Validation
phoneFlag = phone.isdigit() and len(phone) == 10

# Validation Results
print("Validation Results:")
if nameFlag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (must contain only letters and spaces)")

if ageFlag:
    print("Age: Valid ({} years old)".format(age))
else:
    print("Age: Invalid (must be a number between 18 and 65)")

if phoneFlag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (must be exactly 10 digits)")

# Formatted Output
print("\nFormatted Information:")
print("Name: {}".format(name.upper()))

if 18 <= age <= 30:
    print("Age Group: Young Adult (18-30)")
elif 31 <= age <= 50:
    print("Age Group: Adult (31-50)")
else:
    print("Age Group: Mature (51-65)")

print("Phone: +66-{}".format(phone))