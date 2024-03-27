# The following functions can be used to replicate their equivalent Redis command.
# Generally they can be used as functions on your redis connection.
# For the simplest example, see below:

# Getting and settings data in redis

import redis
r = redis.Redis(decode_responses=True)
r.set('mykey', 'thevalueofmykey')
r.get('mykey')  # => "thevalueofmykey"

# Incrementing and decrementing values in redis
def increment_by(conn, key, amount=1):
    return conn.incr(key, amount)

def decrement_by(conn, key, amount=1):
    return conn.decr(key, amount)

print(increment_by(r, 'mykey'))   # => 1
print(decrement_by(r, 'mykey'))   # => 0