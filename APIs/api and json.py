import json
import requests
# lst = [1,2,3]
# print(lst[0])
# data = open("test.json", "r")
# print(data.read())
# print(type(data))
# myobj = json.load(data)
# print(type(myobj))
# print(myobj[1]["Salary"])

# obj = {"Employee1":
#            {
#                "name":"Mohit",
#                "skills":"Django"
#            },"Employee2":
#            {
#                "name":"Yash",
#                "skills":"React"
#            }}
# print(type(obj))
# jsondata = json.dumps(obj)
# print(type(jsondata))
# f = open("new.json", "w")
# f.write(jsondata)

url = "https://jsonplaceholder.typicode.com/todo"
# response = requests.get(url)
# print(type(response.text))
# responseobj = json.loads(response.text)
# print(type(responseobj))
# print(responseobj[0]["title"])


response = requests.post(url, data={"userid":1,
                                    "title":"My New Title"})
print(response.status_code)
