names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search = input("Input the name of who you are looking for: ").capitalize()

if search in names:
    index = names.index(search) + 1
    print(f"{search} was found at index num {index}.")
else:
    print(f"{search} does not exist in the list.")