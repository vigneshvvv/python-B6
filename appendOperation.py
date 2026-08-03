lines = ["java\n", "python\n", "JavaScript\n"]

with open("note.txt", "a") as f:
    f.write("This is append operation\n")
    f.writelines(lines)