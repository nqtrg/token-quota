from datetime import datetime

import redis

from config import DATETIME_FMT, BILLING_PERIOD, MAX_TOKENS


class Quota(object):
    def __init__(self, redis_host: str, redis_port: int):
        self.redis_connection_str = redis_connection_str
        self.redis_bucket = redis.Redis(host=redis_host, port=redis_port, db=0)


    def is_qualified(self, key: str: str, num_tokens: int=1) -> bool:
        period_started_at = self._get_period_started_at(key)
        latest_period_started_at = self._get_deserved_period_started_at(period_started_at)

        if latest_period_started_at != period_started_at:
            # reset token
            self._reset_quota(key)
            # get left token
            left_tokens = MAX_TOKENS

        else:
            # get left token
            left_tokens = self._get_left_token(key)

        if left_tokens > num_tokens:
            left_tokens = left_tokens - num_tokens
            # update left token to storage
            self._update_quota(key, left_tokens, latest_period_started_at)
            return True

        return False

    def _update_quota(self, key: str, left_tokens, period_started_at):
        self.redis_bucket.set(key, json.dumps(
                {
                    "tokens": left_tokens,
                    "period_started_at": period_started_at
                }
            ))

    def _get_left_token(self, key: str):
        # Get left token
        result_json = self.redis_bucket.get(key)
        result = json.loads(result_json)
        return result['tokens']

    def _get_deserved_period_started_at(self, period_started_at):
        current_ts = datetime.now()
        abs((d2 - d1).months) > 1

        pass

    def _get_period_started_at(self, key: str) -> datetime:
        result_json = self.redis_bucket.get(key)
        result = json.loads(result_json)
        return datetime.strptime(result['period_started_at'], DATETIME_FMT)

    def _reset_quota(self, key: str):
        pass
