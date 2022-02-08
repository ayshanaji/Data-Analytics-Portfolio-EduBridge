"""import modulecal as mod"""
"""Another method is to take the specified func"""
"""from modulecal import validate_and_execute,user_name_message
user_input =""
while user_input != "exit":
    user_input = input(user_name_message)
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_units_dictionary)
    print(type(days_and_units_dictionary))
    validate_and_execute(days_and_units_dictionary)"""
import logging
logger= logging.getLogger("main")
logger.error("error happened")
