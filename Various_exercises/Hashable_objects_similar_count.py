from collections.abc import Hashable

object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
hash_val_list = []
count = 0
for i in object_list:
    if isinstance(i, Hashable):
        hash_val_list.append(hash(i))
for i in set(hash_val_list):
    n = hash_val_list.count(i)
    if n > 1:
        count += n
        
print(count)

