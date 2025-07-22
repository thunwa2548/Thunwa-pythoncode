# Complete this program to classify people by age
# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

age = int(input("Enter your age: "))
if age<=12:
    print("You are Child")
elif age<=19:
    print("You are Teenager")
elif age<=59:
    print("You are Adult")
else:
    print("you are senior")