from datetime import datetime

import redis

BILLING_PERIOD = '1m'  # 1 month

# MAX_TOKENS = {
#     "FREE_TIER": 100,
#     "PREMIUM": 10000,
#     "ENTERPRISE": 1000000
# }

MAX_TOKENS = 3

class Quota(object):
    def __init__(self, redis_host: str, redis_port: int):
        self.redis_connection_str = redis_connection_str
        self.redis_bucket = redis.Redis(host=redis_host, port=redis_port, db=0)


    def is_qualified(self, key: str, num_tokens: int=1) -> bool:
        latest_period_started_at = self._get_deserved_period_started_at(key)
        period_started_at = self._get_period_started_at(key)
        if latest_period_started_at != period_started_at:
            # reset token
            self._reset_quota(key)
            # get left token
            left_tokens = MAX_TOKENS

        else:
            # get left token
            left_tokens = self._get_token_count(key)

        if left_tokens > num_tokens:
            left_tokens = left_tokens - num_tokens
            # update left token to storage
            self._update_quota(key, left_tokens, latest_period_started_at)
            return True

        return False

    def _update_quota(self, key, left_tokens, period_started_at):
        self.redis_bucket.set(key, json.dumps(
                {
                    "tokens": left_tokens,
                    "period_started_at": period_started_at
                }
            ))

    def _get_token_count(self, key):
        pass

    def _get_deserved_period_started_at(self, key):
        pass

    def _get_period_started_at(self, key):
        pass

    def _reset_quota(self, key):
        pass
