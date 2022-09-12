template = input("template: ")
print("data:\n")
data=[]
line = input().strip()
while line != "":
    arr = line.split("\t")
    data.append(arr)
    line = input().strip()

for row in data:
    print(template.replace("***", row[0]))