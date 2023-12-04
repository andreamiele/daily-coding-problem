def process_line(line):
    # Find the first and last digits in the line
    first_digit = next((char for char in line if char.isdigit()), None)
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)

    # Combine to form a two-digit number
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    else:
        return 0

def main():
    total_sum = 0
    with open("inputd1.txt", "r") as file:
        for line in file:
            total_sum += process_line(line.strip())

    print(f"Total sum of calibration values: {total_sum}")

#if __name__ == "__main__":
    #main()

#!/usr/bin/python3

DIGITS = {
    "one": 1, 
    "two": 2,
    "three": 3, 
    "four": 4,
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9, 
    "zero": 0
    }

def find_digit(s):

    substr = ""

    for char in s:
        if char.isdigit():
            return char
        
        substr += char

        for d in DIGITS.keys():
            if d in substr:
                return str(DIGITS[d])
            elif d[::-1] in substr:
                return str(DIGITS[d])
    
    return None

def score_line(line):
    first_digit = find_digit(line)
    last_digit = find_digit(reversed(line))
    

    if first_digit == None and last_digit == None:
        return 0
    else:
        return int(first_digit + last_digit)


def main():

    count = 0

    with open("inputd1.txt", "r") as f:
        for line in f:
            count += score_line(line)

    print(count)

    return


if __name__ == "__main__":
    main()
