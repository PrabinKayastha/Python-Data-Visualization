import requests
import json


# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status Code : {r.status_code}")


# Explore the structure of data.
response_dict = r.json()
readable_file = 'output-files/readable_hacker_news_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)