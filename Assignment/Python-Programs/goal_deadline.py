import datetime
user_input=input("Hello user!,Enter the goal and deadline :\n")
input_list=user_input.split(":")
goal= input_list[0]
deadline=input_list[1]
deadline_date=datetime.datetime.strptime(deadline,"%d.%m.%Y")
print(deadline_date)
today_date=datetime.datetime.today()
time_till=deadline_date -today_date
print(f"Dear user!,Time remainning for your{goal}is {time_till}")
print(f"Dear user!,Time remainning for your{goal}is {time_till.days}days")
print(f"Dear user!,Time remainning for your{goal}is {time_till.seconds}hours")
print(f"Dear user!,Time remainning for your{goal}is {time_till.seconds/60/60} hours")