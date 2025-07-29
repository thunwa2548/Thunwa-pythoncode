"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""
def personal_info_manager():
    # Create initial person tuple
    person = ("Thunwa", "19", "Suratthani", "Thai")  # name, age, city, country
    hobbies = []
    while true
    choice=input('please choice 1-5')
    if choice == '1' :
    print('name :',person[0])
    print(f"age :(person[1])")
    print("city :" +person[2])
    print("Country :",person[3])
    print("hobby:",hobbies)

    elif choice=='2' :
    hobby=input("What is new hobbies :")
    hobbies.append[hobby]
    
    elif choice=='3' :
    hobbies.pop()
    elif choice=='4' :
    person_list=list(person)
    age=input("How old are you")
    person_list[1]=age
    person=tuble(person_list)


    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()
