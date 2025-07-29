def number_operations():
    numbers = []

    # รับเลขจากผู้ใช้จำนวน 10 ค่า
    print("Enter 10 numbers:")
    for i in range(10):
        number = int(input('insert number'))
    print(f"Original bumber: {numbers}")  
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    average = sum(numbers) / len(numbers)
    above_average = [num for num in numbers if num > average]
    print(f"\nเลขคู่: {even_numbers}")
    print(f"เลขคี่: {odd_numbers}")
    for i in range(10):
        number = int(input('insert number["+i+"]:'))
        numbers.append(numbers)
        if numbers[i]%2==0 :
            even_numbers.append(number[i])
        else :
            odd_numbers.append(number[i])
        if number[i]>average.append(number[i]):
            above_average.append(number[i])
        print('even number list',even_numbers)
        print('add number list',odd_numbers)
        print('above average',above_average)
        print('min',min(numbers))
        print('max',max(numbers))
    print(f"ค่าเฉลี่ย: {average:.2f}")
    print(f"ตัวเลขที่มากกว่าค่าเฉลี่ย: {above_average}")
if __name__ == "__main__":
    number_operations()