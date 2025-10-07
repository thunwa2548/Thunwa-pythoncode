"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():
    temps = []
    print("temperatures in 7 day")
    for i in range(7):
        temp = float(input(f"day {i+1}: "))
        temps.append(temp)
    return temps
    
def analyze_temps(temp_list):
    avg = sum(temp_list) / len(temp_list)
    high = max(temp_list)
    low = min(temp_list)
    return avg, high, low

def display_analysis(avg, high, low):
    print("\nTemperature in a week: ")
    print(f"Average: {avg:.1f} c")
    print(f"Highest: {high:.1f} c")
    print(f"Lowest: {low:.1f} c")

def main():
    temps = get_temperatures()
    avg, high, low = analyze_temps(temps)
    display_analysis(avg, high, low)

main()