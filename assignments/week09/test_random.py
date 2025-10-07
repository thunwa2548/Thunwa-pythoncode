import random

def test_random():
    # สุ่มเลขระหว่าง1-10เก้ยไว้ในตัวแปรชื่อ random_number
    random_number = random.randint(1, 100)

    #รับค่าจากการทายเลขของผู้ใช้ เก็บไว้ในตัวแปรชื่อguess_number
    guess_number = input("What is you guess number?:")

    if random_nimber ==guess_number:
        print("Congratulation")

    elif random_number < guess_number:
        print("Too much")
    elif random_number > guess_number:
        print ("Too low")

    print(random_number)
    
test_random()