
def solution():
    left = []
    right = []
    with open("inputs/day1input.txt") as file: #open the text file
        for line in file:
            left_string, right_string = line.split() #for each line in file, split the line by the space between the two strings and store in two variables
            left.append(int(left_string)) #add left string to left list
            right.append(int(right_string)) #add right string to right list
        
    #sort the lists in ascending order so we can compare the smallest in each list, second smallest in each list etc
    left = sorted(left)
    right = sorted(right)

    #zip the lists together, then we compare each element in each tuple
    distance = 0
    for tuple in zip(left,right):
        distance += abs(tuple[0] - tuple[1])

    print("part 1 answer:", distance) #part 1 answer

    score = 0
    for number in left: #for each number in the left list, count how many times it is in the right list and update score accordingly
        score += (number * right.count(number))
    
    print("part 2 answer:", score) #part 2 answer


solution()
