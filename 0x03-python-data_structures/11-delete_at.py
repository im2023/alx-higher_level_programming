def delete_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return my_list

    x = []
    for i in range(len(my_list)):
        if i != idx:
            x.append(my_list[i])

    return x
