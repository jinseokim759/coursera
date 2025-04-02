nums = [1, 2, 2, 4, 3, 3, 3, 5, 7, 5, 6, 6, 7, 8, 5, 5, 5, 9]
# 1:1, 2:2, 3:3, 4:1, 5:5, 6:2, 7:2, 8:1, 9:1

def most_num_in_list(list):
    list.sort()                 
    j = 0                       #for count
    num, cnt = 0, 0             
    for i in range(len(list)):  
        if list[i] != list[j]:  #when i moved to the next num
            if i - j > cnt:     #check that num is the most frequent
                num = list[j]   #change num
                cnt = i - j     #change count
            j = i               #move j to next num
    return num

def mNIL2(list):
    num, cnt = 0, 0
    cnt_dict = {}                   #dict stores num(key) and frequency(value)
    for i in range(len(list)):
        if list[i] in cnt_dict:     #check num is in dict
            cnt_dict[list[i]] += 1  #count +1 if it is
        else:
            cnt_dict[list[i]] = 1   #make new if it is not

        if cnt_dict[list[i]] > cnt: #tracking most frequent num
            num = list[i]
            cnt = cnt_dict[list[i]]

    return num

#num = most_num_in_list(nums)
#print("Most frequent number in the list is " + str(num) + ".")
print(mNIL2(nums))