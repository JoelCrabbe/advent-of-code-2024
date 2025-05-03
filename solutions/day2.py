def solution():
    with open("inputs/day2input.txt") as file:
        part_1_safe_count = 0
        part_2_safe_count = 0
        for line in file: #loop through each line in the file
            temp_list = line.split() #temp_list is a list of each string(number) in the line
            list = []
            for item in temp_list:
                list.append(int(item)) #turn the strings into ints

            if is_safe_part_1(list) == 1: 
                part_1_safe_count += 1
            
            elif is_safe_part_two(list) > 0: 
                part_2_safe_count += 1

            
            
        print("part 1 answer:", part_1_safe_count)
        print("part 2 answer:", part_1_safe_count + part_2_safe_count)
                
                

def is_safe_part_1(list):
    if list == sorted(list) or list == sorted(list,reverse=True): #if the list is all increasing or all decreasing
        safe = True
        for i in range(len(list) - 1): # we check whether adjacent elements differ by at least 1 or 3, if that is true for all elements then we have found a safe list
            if not (abs(list[i] - list[i+1]) >= 1 and abs(list[i] - list[i+1]) <= 3):
                safe = False
                
        if safe: return 1
    return 0

def is_safe_part_two(list):
    #want to call is_safe on each list obtained by removing one element in list
    smaller_list_safe_count = 0
    for i in range(len(list)):
        temp = [list[j] for j in range(len(list)) if j != i] #we check whether each list obtained by removing one element is safe. If any are, then the original list is part 2 safe
        smaller_list_safe_count += is_safe_part_1(temp)
    return smaller_list_safe_count

         
solution()



        
