import re

MAPPING_ARRAY = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def main():
    total = 0
    with open("input.txt", "r") as input_file:
        for line in input_file.readlines():
            matches = re.findall(r"(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))", line)
            numbers = [MAPPING_ARRAY.get(match, match) for match in matches]

            total += int(f"{numbers[0]}{numbers[-1]}")

    print(total)


if __name__ == '__main__':
    main()
