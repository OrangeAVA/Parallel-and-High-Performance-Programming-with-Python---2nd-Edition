from dramatiq import group
from dramaserver_results import wait
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend
import dramatiq

broker = RedisBroker(host="localhost")
dramatiq.set_broker(broker)
result_backend = RedisBackend(host="localhost")
broker.add_middleware(Results(backend=result_backend))

g = group([
    wait.message(10, 'A'),
    wait.message(5,  'B'),
    wait.message(4,  'C'),
    wait.message(7,  'D'),
]).run()

for res in g.get_results(block=True, timeout=12000):
    print(res)

print("End Program")
