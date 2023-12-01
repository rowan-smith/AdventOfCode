DATA_FILE = []

# Example = 142

total = 0
with open("input.txt", "r") as input_file:
    for line in input_file.readlines():
        result = [character for character in line if character.isnumeric()]
        total += int(f"{result[0]}{result[-1]}")

print(total)
