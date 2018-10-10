import requests

from operator import itemgetter

# Make an API call and store the response

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

# Process the information
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make separate API call for each submission
    url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json")
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    submission_dict = {
        'title' : response_dict['title'],
        'link' : 'https://news.ycombinator.com/item?id=' + str(submission_id),
        'comments' : response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for item in submission_dicts:
    print("\nTitle : ", item['title'])
    print("Discussion link : ", item['link'])
    print("Comments : ", item['comments'])
