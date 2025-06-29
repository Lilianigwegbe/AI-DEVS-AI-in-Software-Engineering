#Given a list below:
#Data that makes up the Dictonary
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

#Manual Python Code
def sort_by_key_manual(data, key):
    sorted_list = []
    for item in data:
        inserted = False
        for i in range(len(sorted_list)):
            if item[key] < sorted_list[i][key]:
                sorted_list.insert(i, item)
                inserted = True
                break
        if not inserted:
            sorted_list.append(item)
    return sorted_list
