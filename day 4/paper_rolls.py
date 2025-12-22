


def paper_rolls(file_name):
    with open(file_name, 'r') as f:
        rolls = f.read()
    print(rolls, len(rolls))

    length = len(rolls)
    total = 0
    previous = 0
    curr = 0
    for i in range(8):
        while 


def main():
    file_name = "test4.txt"
    print(paper_rolls(file_name))

if __name__ == "__main__":
    main()