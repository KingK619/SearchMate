# Google Search the query statement and get all the results as in json format
import json
from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    formatedJson = json.dumps(res, indent=2)
    return formatedJson


