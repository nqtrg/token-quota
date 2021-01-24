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
