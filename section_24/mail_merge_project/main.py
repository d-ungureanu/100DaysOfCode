new_list = []
with open("./Input/Names/invited_names.txt", "r") as names_file:
    names_list = names_file.readlines()

    for name in names_list:
        new_list.append(name.strip("\n"))

with open("./Input/Letters/starting_letter.txt", "r") as lt:
    letter_template = lt.read()
    for name in new_list:
        letter_content = letter_template.replace("[name]", name)
        file_name = f"./Output/ReadyToSend/letter_for_{name}.txt"
        with open(file_name, "w") as personal_letter:
            personal_letter.write(letter_content)
