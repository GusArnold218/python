minutes_input = input("Please, enter the number of minutes: ")

total_minutes = int(minutes_input)


hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"{total_minutes} is {hours} hours and {remaining_minutes} minutes")
