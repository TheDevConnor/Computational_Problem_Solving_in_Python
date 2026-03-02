file_name = input("Enter filename: ")

try:
    f = open(file_name, "w")
except FileNotFoundError:
    print("File not found.")
else:
    f.write("This is a test\n")
    f.close()
    print("File written successfully.")
finally:
    print("Finished attempt.")

print("End of program.")
