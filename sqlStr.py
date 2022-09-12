mode = input("insert or update?")

lines=[]
line = input().strip()
while line != "":
    lines.append(line)
    line = input().strip()

for line in lines:
    print(line)
