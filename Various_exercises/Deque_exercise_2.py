from collections import deque 
my_queue = deque()

for i in ['READY Anna', 'READY Tom', 'EXTRA', 'PASSED', 'PASSED']:
    my_input = i.split()
    if my_input[0] == 'READY':
        my_queue.append(my_input[1])
    elif my_input[0] == 'EXTRA':
        my_queue.append(my_queue.popleft())
    elif my_input[0] == 'PASSED':
        print(my_queue.popleft())


