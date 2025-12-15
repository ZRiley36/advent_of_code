

def count_zeros(file_name):
    f = open(file_name, "r")
    lines = f.readlines()
    count = 50
    add = False
    zero_hits = 0
    for line in lines:
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

    return zero_hits




def main():
    file_name = "input.txt"
    print(count_zeros(file_name))

if __name__ == "__main__":
    main()
