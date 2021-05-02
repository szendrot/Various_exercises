def add_viewer(name, *args):
    if len(args) == 0:
        return [name]
    else:
        i = []
        for i in args:
            i.append(name)
        return i
               

name_list = ['Harry', 'Nelly']

print(add_viewer('Molly', name_list))

