# with open("test.txt", "r+") as f:
#     contents = f.read()
#     print(contents)

with open("test.txt", mode="r+") as f:
    old_content = f.read()
    print(old_content)
    f.write("New text line after reading")
    new_content = f.read()
    print(new_content)