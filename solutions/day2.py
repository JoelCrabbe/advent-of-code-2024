def solution():
    with open("inputs/day2input.txt") as file:
        safe_count = 0
        part_2_safe_count = 0
        for line in file: #loop through each line in the file
            temp_list = line.split() #temp_list is a list of each number in the line
            list = []
            for item in temp_list:
                list.append(int(item)) #turn the strings into ints

            if is_safe(list) == 1:
                safe_count += 1
            
            elif is_safe_part_two(list) > 0:
                part_2_safe_count += 1

            
            
        print("part 1 answer:", safe_count)
        print("part 2 answer:", safe_count + part_2_safe_count)
                
                

def is_safe(list):
    if list == sorted(list) or list == sorted(list,reverse=True): 
        safe = True
        for i in range(len(list) - 1):
            if not (abs(list[i] - list[i+1]) >= 1 and abs(list[i] - list[i+1]) <= 3):
                safe = False
                
        if safe: return 1
    return 0

def is_safe_part_two(list):
    #want to call is_safe on each list obtained by removing one element in list
    smaller_list_safe_count = 0
    for i in range(len(list)):
        temp = [list[j] for j in range(len(list)) if j != i]
        smaller_list_safe_count += is_safe(temp)
    return smaller_list_safe_count

         
solution()



        
