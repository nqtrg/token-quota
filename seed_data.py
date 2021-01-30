import json
from datetime import datetime, timezone

from config import DATETIME_FMT

datetime_now = datetime.now(timezone.utc)


seed_data = {
    # key: [tokens, period_started_at]
    "nqtrg": {
        "tokens": 1000,
        "subcription": "FREE_TIER",
        "period_started_at": datetime.strftime(datetime_now, DATETIME_FMT)
    },
    # "limmie": {
    #     "tokens": 700,
    #     "subcription": "FREE_TIER",
    #     "period_started_at": "2021-01-23T18:25:43.511Z"
    # },
}

import redis
r = redis.Redis(host='localhost', port=6379, db=0)

for key in seed_data:
    r.set(key, json.dumps(seed_data[key]))

# test
result_json = r.get('nqtrg')
result = json.loads(result_json)
assert(result['tokens'] == 1000)
print(datetime.strptime(result['period_started_at'], DATETIME_FMT))
print(datetime_now)
assert datetime.strptime(result['period_started_at'], DATETIME_FMT) == datetime_now
