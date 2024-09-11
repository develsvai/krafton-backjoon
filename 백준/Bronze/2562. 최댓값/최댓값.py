def find_index_max(arr) : 
    
    tmp = arr[0]
    tmp_index =0 
    
    for i in range(len(arr)) :
        if arr[i] > tmp :
            tmp = arr[i]
            tmp_index = i
    return tmp , tmp_index+1


num = []

for i in range(9) : 
    

    user_input = input()

    if user_input == "" :
        break

    num.append(int(user_input))


max_val, max_index = find_index_max(num)

print(max_val)
print(max_index)