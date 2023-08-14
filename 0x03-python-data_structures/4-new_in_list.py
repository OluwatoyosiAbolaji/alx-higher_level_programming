#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_copy = []
    if idx < 0 or idx > len(my_list):
        for index in my_list:
            my_list_copy.append(index)
    else:
        for index in range(len(my_list)):
            if index == idx:
                my_list_copy.append(element)
            else:
                my_list_copy.append(my_list[index])
    return my_list_copy
