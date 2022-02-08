def first_last_number(number_list):
    print("The list is:",number_list)
    first_num= number_list[0]
    last_num=number_list[-1]
    if first_num == last_num :
        return True
    else:
        return False
num_list=[102,34,45,67,102]
print("The output is :",first_last_number(num_list))
num_list=[102,34,45,67,109]
print("The output is :",first_last_number(num_list))