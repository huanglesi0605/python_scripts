mode = input("insert or update? ")
objName = input("object name? ")

data=[]
line = input().strip()
while line != "":
    arr = line.split("\t")
    data.append(arr)
    line = input().strip()

sqlStr = ""
if mode.lower() in ("u", "update"):
    sqlStr = "update  set "
    for row in data:
        sqlStr += f"{row[0]}=@{row[0]}, "
    sqlStr = sqlStr.rstrip(", ")
    sqlStr += " where id=@id"
elif mode.lower() in ("i", "insert"):
    sqlStr = "insert into  ("
    for row in data:
        sqlStr += f"{row[0]}, "
    sqlStr.rstrip(", ")
    sqlStr += ") values ("
    for row in data:
        sqlStr += f"@{row[0]}, "
    sqlStr.rstrip(", ")
    sqlStr += ")"

print(sqlStr)
print()

if objName != "":
    objName+="."

if mode.lower() in ("u", "update"):
        print(f"new SqlParameter(\"@id\", {objName}id),")

for row in data:
    if "char" in row[1] or "text" in row[1]:
        print(f"new SqlParameter(\"@{row[0]}\", string.IsNullOrWhiteSpace({objName}{row[0]}) ? (object)DBNull.Value : {objName}{row[0]}),")
    else:
        print(f"new SqlParameter(\"@{row[0]}\", {objName}{row[0]}),")



