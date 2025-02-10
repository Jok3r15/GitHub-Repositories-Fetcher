import requests

response = requests.get("https://api.github.com/users/Jok3r15/repos")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\n Project Url: {project['html_url']}\n")
