def days_to_units(num_of_days,conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24*60} minutes"
    else:
        return "unsupported unit"
def validate_and_execute():
    try:
        user_input_number=int(days_and_units_dictionary["days"])
        if user_input_number>0:
            cal_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(cal_value)
        elif user_input_number == 0:
            print( "your number is zero")
    except ValueError:
        print("you entered an invalid number")
user_input =""
while user_input != "exit":
    user_input = input("Enter a list of elements and conversion units to :\n")
    days_and_units = user_input.split(":")
    days_and_units_dictionary ={"days":days_and_units[0], "unit":days_and_units[1]}
    print(days_and_units_dictionary )
    print(type(days_and_units_dictionary ))
   validate_and_execute()