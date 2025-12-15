
def add_ids(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        ints = line.split(',')
        for i in range(ints[0], ints[1] + 1):
            if str(i) == str(i)[::-1]:
                if str(i).length() % 2 == 0:
                    total += i
    return total


def main():
    file_name = "input.txt"
    print(add_ids(file_name))

if __name__ == "__main__":
    main()  