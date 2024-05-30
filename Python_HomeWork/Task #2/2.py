string = list(input("Enter the string: "))
string = [element.lower() for element in string]

stringKey = list(set(string))
if stringKey.count(" "):
    stringKey.remove(" ")

stringDict = {stringKey[i]: string.count(stringKey[i]) for i in range(len(stringKey))}

print(
    "Dictionary of the form {“character”: “number of characters in line”}: ", stringDict
)
