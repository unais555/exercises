with open("data.txt","r") as file:
    line_no = 1
    for line in file:
        print(f"{line.strip()} is on line {line_no}")
        line_no += 1

name = input("Enter a name : ")
with open("data.txt", "r") as file:
    line_no = 1
    flag = 0
    for line in file:
        if line.strip() == name:
            flag = 1
            break
        line_no += 1
if flag == 1:
    print(f"{name} is on line {line_no}")
else:
    print("No such name exists")

with open("data.txt","r") as file:
    data = file.read()
    words = data.split()

print(f"Total number of words : {len(words)}")