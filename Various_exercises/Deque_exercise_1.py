from collections import deque

for i in range(int(4)):
    my_queue = deque()
    my_input = 'ENQUEUE 1'.split()
    if my_input[0] == 'ENQUEUE':
        my_queue.append(my_input[1])
    else:
        my_queue.pop()
for i in my_queue:
    print(i)
