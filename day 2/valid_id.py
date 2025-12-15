
def add_ids(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    print(text)


    total = 0
   
    ranges = text.split(',')
    for r in ranges:
        ints = r.split('-')
        first = int(ints[0])
        second = int(ints[1]) + 1
        for i in range(first, second):
            if len(str(i)) % 2 == 0:
                first_half = str(i)[:len(str(i))//2]
                second_half = str(i)[len(str(i))//2:]  
                if first_half == second_half:
                    print(f"invalid id: {i}")
                    total += i
    return total


def main():
    file_name = "input2.txt"
    print(add_ids(file_name))

if __name__ == "__main__":
    main()