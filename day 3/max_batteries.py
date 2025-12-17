def max_batteries(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    total = 0
    for battery in lines:
        print(battery)
        battery = battery.strip('\n')

        tens_digit = len(battery) - 2
        ones_digit = len(battery) - 1
        highest_ten = int(battery[tens_digit])
        highest_one = int(battery[ones_digit])
        while tens_digit >= 0 :
            if int(battery[tens_digit]) >= highest_ten:
                if highest_one < highest_ten:
                    highest_one = highest_ten
                highest_ten = int(battery[tens_digit])
            tens_digit -= 1
        print(f"battery: {int(highest_ten) * 10 + int(highest_one)}")
        total += int(highest_ten)*10 + int(highest_one)
    return total


def main():
    file_name = "input3.txt"
    print(max_batteries(file_name))

if __name__ == "__main__":
    main()