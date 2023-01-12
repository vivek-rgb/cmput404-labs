import requests
print(requests.__version__)

response = requests.get("http://www.google.com/")

print("PRINTING RESPONSE: ")
print(response)

file_download = requests.get("https://raw.githubusercontent.com/vivek-rgb/cmput404-labs/master/lab1.py")
print(file_download.text)