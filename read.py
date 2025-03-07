import json
PathToFile = "C:\\Users\\sbane\\Downloads\\student.json"  


with open(PathToFile, "r") as file:
   jsonstr = file.read()

jsonObj = json.loads(jsonstr)

print("JSON DATA AS DICTIONARY:", jsonObj)

print("Student Name:",jsonObj["name"])
print("Student Major:",jsonObj[ "Intented Major"])
print("Student Course:",jsonObj["Currently enrolled in Course "])

jsonObj["name"] = "Ummul Baneen" 

with open(PathToFile, "w") as file:
   json.dump(jsonObj, file, indent=4)

print("Students name updated successfully")
print(jsonObj["name"])

