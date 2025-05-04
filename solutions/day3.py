import re

def part_1_solution():
    with open("inputs/day3input.txt") as file:
        contents = file.read()
        # searches for mul then a ( then 1-3 digits then a , then 1-3 digits then a ). I put the digits bit into a group to easily access them late with match.group()
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)") #could have also done \d+ to keep searching for digits until the , or last )
        matches = pattern.finditer(contents)
        sum = 0
        for match in matches:
            sum += (int(match.group(1)) * int(match.group(2)))
        print("part 1 answer:",sum)


def part_2_solution():
    with open("inputs/day3input.txt") as file:
        contents = file.read()
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)") # we are searching for all three patterns
        matches = pattern.finditer(contents)
        sum = 0
        last_seen = "" # keep track of the command we last saw
        for match in matches:
            if match.group(0).startswith("mul") and last_seen != "don't()": #if command is mul and we didnt last see a dont, do the mul command
                sum += (int(match.group(1)) * int(match.group(2)))
                last_seen = "mul" 

            elif match.group(0) == "don't()": 
                last_seen = "don't()"
            
            elif match.group(0) == "do()":
                last_seen = "do()"
                

        print("part 2 answer:",sum)


part_2_solution()
