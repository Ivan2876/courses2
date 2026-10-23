import time
from redis_utils.redis_client import redis_client



for pub in range(0,9):
    time.sleep(0.5)
    redis_client.publish('Hello Redis!', f'message #{pub}')