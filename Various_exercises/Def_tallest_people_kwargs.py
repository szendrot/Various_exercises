def tallest_people(**kwargs):
    max_height = 0
    result = {}
    for i in kwargs:
        if kwargs[i] == max_height:
            result[i] = kwargs[i]
        elif kwargs[i] > max_height:
            max_height = kwargs[i]
            result = {i: kwargs[i]}
    
    for key, value in sorted(result.items()):
        print(key + ' : ' + str(value))

tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)

