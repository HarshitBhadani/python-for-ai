import requests

print("Hello World!!")
response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Successfully connected to GitHub API")

age = 25
score = -10
pi = 3.14159
flag = True
fname = "Harshit"
lname = "Kumar"

print(f"Age: {age}, Score: {score}, Pi: {pi}")
print(f"Name: {fname} {lname} {len(fname)} {len(lname)}")

flag = age>56 and score<0
print(f"Flag: {flag}")

print(True or False)
print (True and False)
print (not True)

score = "10" + f"Score is {score}"
print(score)

text = "python programming"
text.upper()
text.lower()
text.title()

print("Python" in text)
print(text.find("programming"))
print(text.replace("python", "java"))

temp = 25
if temp>30:
    print("It's hot outside")
else:
    print("It's not that hot outside")

for i in range(5):
    print(f"Iteration {i}")

for i in range(2,15,2):
    print(f"Iteration {i}")

#List
my_list = ["Alice",25,False,3.14]
print(my_list)

#Dictionary
my_dict = {"name":"Alice", "age":25, "is_student":False}    
print(my_dict)
print(my_dict["name"])
my_dict["license"] = True
print(my_dict)
del my_dict["age"]
print(my_dict)
print(my_dict.get("age", "Age not found"))
print(my_dict.keys())
print(my_dict.values())

#tuple
point = (10, 20) 
print(point)