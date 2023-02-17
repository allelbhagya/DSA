### Hashing

Hashing is a process of taking an input data (such as a string or a file) and transforming it into a fixed-size output called a hash value or a digest. The hash value is typically a unique and representative "fingerprint" of the input data, and it is generated using a hashing algorithm.

Hashing means using some function or algorithm to map object data to some representative integer value.

This so-called hash code (or simply hash) can then be used as a way to narrow down our search when looking for the item in the map.

```python
my_hash_table = {}
my_hash_table = dict()
key,value = 1, 'first'
# Insertion
my_hash_table[key] = value

value = my_hash_table.get(key) # returns None if the key is not present
value = my_hash_table[key] # throws a ValueError exception if the key is not present

my_hash_table[2] = 'second'
my_hash_table[3] = 'third'

del my_hash_table[key] # throws a ValueError exception if the key is not present

keys = my_hash_table.keys()
values = my_hash_table.values()
print(my_hash_table)
```
