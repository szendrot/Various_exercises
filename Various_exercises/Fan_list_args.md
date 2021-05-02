# put your python code here
word_list = [word.lower() for word in input().split()]
word_dict = {}
for word in word_list:
    try:
        word_dict[word] += 1
    except KeyError:
        word_dict[word] = 1
for key, value in word_dict.items():
    print(key, value)
