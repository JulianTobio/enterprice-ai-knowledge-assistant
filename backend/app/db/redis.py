from redis import Redis
from rq import Queue
from app.core.config import QUEUE_HOST, QUEUE_NAME, QUEUE_PORT

redis_conn = Redis(host=QUEUE_HOST, port=QUEUE_PORT)
q = Queue(QUEUE_NAME, connection=redis_conn)

def get_queue():
    return q