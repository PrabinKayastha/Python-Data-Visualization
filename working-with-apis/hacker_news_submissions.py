from operator import itemgetter
from pprint import pprint
import requests

# ake an API call and store the reponse.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status Code : {r.status_code}')

# Process the information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make new API call for each submissions.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'ID :{submission_id}\tStatus : {r.status_code}')
    response_dict = r.json()

    
