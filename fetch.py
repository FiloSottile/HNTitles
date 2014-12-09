import requests
import time
import sys

url = "https://hn.algolia.io/api/v1/search_by_date?tags=story&numericFilters=created_at_i>{},created_at_i<{},points>50&hitsPerPage=1000"
start_point = time.time() - 3 * 365 * 24*60*60
reached = time.time()
while True:
    r = requests.get(url.format(start_point, reached))
    j = r.json()
    if len(j['hits']) < 1000: break
    for h in j['hits']:
        print h['title'].encode('utf8')
        reached = h['created_at_i']
    sys.stderr.write('.')
    sys.stderr.flush()
sys.stderr.write('\n')