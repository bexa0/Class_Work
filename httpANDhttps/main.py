import requests
import webbrowser

url = 'https://jsonplaceholder.typicode.com/todos'
a = requests.get(url)

a.raise_for_status()
print(a)

# CREATE JSON
with open('dz1.json', 'w')as file:
    file.write(a.text)

url = 'C:\Users\ШухратовБе\PycharmProjects\httpANDhttps\dz1.json'
webbrowser.open_new_tab(url)

webbrowser.open_new_tab(url)