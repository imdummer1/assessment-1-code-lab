def ask(prompt, type_):
    while True:
        value = input(prompt).strip()

        if type_ == int:
            if value.isdigit():
                return int(value)
            print("Please enter a number.")
        else:  # assume string
            if value.isalpha():
                return value
            print("Please enter letters only.")

first_name = ask("Insert your first name: ", str)
second_name = ask("Insert your second name: ", str)
age = ask("Insert age: ", int)
hometown = ask("Insert your hometown: ", str)

print(f"Name: {first_name} {second_name}\nage: {age}\nhometown: {hometown}")