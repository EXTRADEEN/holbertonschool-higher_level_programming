#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if type(my_list_1[i]) not in [int, float]:
                print("wrong type")
                result = 0
            elif type(my_list_2[i]) not in [int, float]:
                print("wrong type")
                result = 0
            elif my_list_2[i] == 0:
                print("division by 0")
                result = 0
            else:
                result = my_list_1[i] / my_list_2[i]
        except (IndexError, TypeError):
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
