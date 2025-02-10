GitHub Repositories Fetcher

Description

This Python script retrieves and displays a list of public repositories for a specified GitHub user using the GitHub API. It fetches repository data and prints the repository name along with its corresponding URL.



Requirements

Python 3.x

requests library (install it using pip install requests if not already installed)



Installation

Ensure you have Python installed on your system.



Install the required dependency:

pip install requests

Download or copy the script to your local machine.



Usage

Run the script with Python:

python script.py



Code Explanation

import requests

response = requests.get("https://api.github.com/users/Jok3r15/repos")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\n Project Url: {project['html_url']}\n")

requests.get(url): Sends an HTTP GET request to the specified URL.

response.json(): Converts the JSON response into a Python dictionary.

Iterates through each repository in the response and prints the repository name and URL.



Notes

The script currently fetches repositories for the GitHub user Jok3r15 (your GitHub username).

This implementation can be modified to work with any GitHub user by replacing Jok3r15 with the desired GitHub user ID.

Ensure you have an active internet connection to make API requests.



License

This project is licensed under the MIT License.
