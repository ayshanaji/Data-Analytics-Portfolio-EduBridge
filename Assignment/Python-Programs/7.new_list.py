def combine_list(list1,list2):
    new_list=[]
    for n in list1:
        if n%2!=0:
            new_list.append(n)
    for n in list2:
        if n %2 ==0:
            new_list.append(n)

    return new_list
list1=[10,23,45,32,56,77,79]
list2=[34,67,78,89,76,55]
print("The combined one list is :",combine_list(list1,list2))