from dramatiq import group
from dramaserver import wait

g = group([
    wait.message(10, 'A'),
    wait.message(5,  'B'),
    wait.message(4,  'C'),
    wait.message(7,  'D'),
]).run()

print("End Program")
