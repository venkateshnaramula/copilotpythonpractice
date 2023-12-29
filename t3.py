import requests

# Task: Make a GET request to 'https://api.example.com/data' and print the response JSON

url = 'https://api.example.com/data'
# Use Copilot to complete the code to make the GET request and print the response JSON
response = requests.get(url)
if response.status_code == 200:
    # Print the response JSON
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f"Request failed with status code {response.status_code}")
# TODO: Print the response JSON
