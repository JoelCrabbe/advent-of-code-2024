import re


def part_1_solution():
    with open("inputs/day4input.txt") as file:
        sum = 0
        contents = file.read()
        pattern = re.compile(r"XMAS|SAMX")
        matches = pattern.finditer(contents)
        for match in matches:
            sum += 1
        
        print(sum)




#part_1_solution()

string = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

sum = 0
pattern = re.compile(r"XMAS|SAMX")
matches = pattern.finditer(string)
for match in matches:
    sum += 1




# print(sum)

