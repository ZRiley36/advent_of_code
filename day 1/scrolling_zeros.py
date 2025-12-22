
def scrolling_zeros(file_name):
    f = open(file_name, "r")
    lines = f.readlines()
    count = 50
    zero_hits = 0
    add = False
    current_dividend = count // 100
    for line in lines:
        previous_dividend = current_dividend
        if line[0] == 'R':
            add = True
        else:
            add = False
        curr_number = int(line[1:])
        if add:
            count += curr_number
        else:
            count -= curr_number

        if count == 0:
            zero_hits += 1
        elif count % 100 == 0:
            zero_hits += 1
        current_dividend = count // 100
        zero_hits += abs(current_dividend - previous_dividend)

    return zero_hits


def main():
    file_name = "../day 1/input.txt"
    print(scrolling_zeros(file_name))

if __name___ == "__main__":
    main()