Redis stands for Remote Dictionary Service.
Redis is an open-source, networked, in-memory database that stores data on the server side and supports data structures such as strings

A Redis database holds key:value pairs and supports commands such as GET, SET, and DEL, as well as several hundred additional commands.

Redis keys are always strings.

Redis values may be a number of different data types, including string, list, hashes, and sets

Many Redis commands operate in constant O(1) time, just like retrieving a value from a Python dict or any hash table.

Redis supports storing additional types of key:value data types besides string:string

# More Data Types in Redis Database 
- Hashes: A collection of key value pairs where the key is a string and associated with a field (also a string) and the value is a list of hashes
1) Hash : It is used to store the data in the form of fields and values pairs
A hash is a mapping of string:string, called field-value pairs, that sits under one top-level key:

Hashes: Commands to operate on hashes begin with an H, such as HSET, HGET, or HMSET

Sets: Commands to operate on sets begin with an S, such as SCARD, which gets the number of elements at the set value corresponding to a given key.

Lists: Commands to operate on lists begin with an L or R. Examples include LPOP and RPUSH. The L or R refers to which side of the list is operated on. A few list commands are also prefaced with a B, which means blocking. A blocking operation doesn’t let other operations interrupt it while it’s executing. For instance, BLPOP executes a blocking left-pop on a list structure.

One noteworthy feature of Redis’ list type is that it is a linked list rather than an array. This means that appending is O(1) while indexing at an arbitrary index number is O(N).

Here is a quick listing of commands that are particular to the string, hash, list, and set data types in Redis:

Type	Commands
Sets	SADD, SCARD, SDIFF, SDIFFSTORE, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SPOP, SRANDMEMBER, SREM, SSCAN, SUNION, SUNIONSTORE

Hashes	HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HINCRBYFLOAT, HKEYS, HLEN, HMGET, HMSET, HSCAN, HSET, HSETNX, HSTRLEN, HVALS

Lists	BLPOP, BRPOP, BRPOPLPUSH, LINDEX, LINSERT, LLEN, LPOP, LPUSH, LPUSHX, LRANGE, LREM, LSET, LTRIM, RPOP, RPOPLPUSH, RPUSH, RPUSHX

Strings	APPEND, BITCOUNT, BITFIELD, BITOP, BITPOS, DECR, DECRBY, GET, GETBIT, GETRANGE, GETSET, INCR, INCRBY, INCRBYFLOAT, MGET, MSET, MSETNX, PSETEX, SET, SETBIT, SETEX, SETNX, SETRANGE, STRLEN
