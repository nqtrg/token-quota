BILLING_PERIOD = '1m'

MAX_TOKENS = {
    "FREE_TIER": 100,
    "PREMIUM": 10000,
    "ENTERPRISE": 1000000
}

seed_data = {
    "nqtrg": {
        "tokens": 1000,
        "period_started_at": "2021-01-23T18:25:43.511Z"
    },
    "limmie": {
        "tokens": 700,
        "period_started_at": "2021-01-23T18:25:43.511Z"
    }
}

class Quota(object):
    def __init__(self):
        pass

    def consume(self, key, num_tokens=1):
        pass

    def get_token_count(self, key):
        pass

    def get_period_start_date(self, key):
        pass

    def reset_quota(self, key):
        pass
