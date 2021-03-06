import json


seed_data = {
    # key: [tokens, period_started_at]
    "nqtrg": {
        "tokens": 1000,
        "period_started_at": "2021-01-23T18:25:43.511Z"
    },
    "limmie": {
        "tokens": 700,
        "period_started_at": "2021-01-23T18:25:43.511Z"
    },
}

import redis
r = redis.Redis(host='localhost', port=6379, db=0)

for key in seed_data:
    r.set(key, json.dumps(seed_data[key]))

# test
result_json = r.get('nqtrg')
result = json.loads(result_json)
assert(result['tokens'] == 1000)
assert(result['period_started_at'] == "2021-01-23T18:25:43.511Z")
