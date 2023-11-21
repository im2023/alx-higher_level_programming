#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    zero_result = 0
    nlst = []
    for i in range(0, list_length):
        try:
            zero_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            zero_result = 0
            print("division by 0")
        except TypeError:
            zero_result = 0
            print("wrong type")
        except IndexError:
            zero_result = 0
            print("out of range")
        finally:
            pass
        nlst.append(zero_result)
    return nlst
