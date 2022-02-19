def pluralize(list_):
    list_pluralized = []
    for item in list_:
        if list_.count(item) > 1:
            if item + 's' not in list_pluralized:
                list_pluralized.append(str(item) + 's')
        
    return list_pluralized


list_ = ['bob', 'jac', 'morris', 'bob']
print(pluralize(list_))