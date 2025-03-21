"""
Sorting a unsorted list
"""
def ex1(ls):
    cmp_idx = 0
    for idx in range(len(ls)):
        cmp_idx = idx + 1
        while cmp_idx < len(ls)-1:
            if ls[idx] > ls[cmp_idx]:
                #print(ls[idx], ls[cmp_idx])
                ls[idx], ls[cmp_idx] = ls[cmp_idx], ls[idx]
                #print(ls)
            cmp_idx += 1
    print(ls)

"""
Merging two sorted lists
"""
def ex2(l1, l2):
    ls = []
    len_list = len(l1) + len(l2)
    #print(len_list)

    for i in range(len_list):
        #print(l1[0], l2[0])
        if len(l1) == 0:
            ls = ls + l2
            break
        elif len(l2) == 0:
            ls = ls + l1
            break
        elif l1[0] <= l2[0]:
            ls.append(l1[0])
            l1.remove(l1[0])
            #print(ls)
        else:
            ls.append(l2[0])
            l2.remove(l2[0])
            #print(ls)
    print(ls)

list1 = [1, 2, 5, 7, 9]
list2 = [3, 4, 6, 8, 10]

list_sum = list1 + list2

ex1(list_sum)
ex2(list1, list2)
list_sum.sort()
print(list_sum)
