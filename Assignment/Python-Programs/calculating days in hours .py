"""cal_units = 24
name_units = "hours"
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * cal_units}{name_units}"
     """"""
"""def validate_and_execute():
    try:
        user_input_number=int(num_of_days_elements)
        if user_input_number>0:
            cal_value = days_to_units(user_input_number)
            print(cal_value)
        elif user_input_number == 0:
            print( "your number is zero")
    except ValueError:
        print("you entered an invalid number")"""
# to input list of elements
"""user_input =""
while user_input != "exit":
    user_input = input("Enter a list of elements and it will convert to hours:")
    list_of_days=user_input.split(",")
    print(type(list_of_days))
    print(type(set(list_of_days)))
    print(list_of_days)
    print(set(list_of_days))
    for num_of_days_elements in set(list_of_days):
        validate_and_execute()"""

d