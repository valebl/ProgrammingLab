def sum_list(my_list):

    if len(my_list) == 0:
        return None
    else:
        sum_list = 0
        for element in my_list:
            sum_list += element

    return sum_list

# Comment the following lines to test the program with Autograding
# if __name__ == '__main__':

#     list1 = [1,2,3,4,5,6,7,8,9, 10]
#     list2 = []
#     sum_list1 = sum_list(list1)
#     sum_list2 = sum_list(list2)
        
#     print("The sum of {} is {}.".format(list1, sum_list1))
#     print("The sum of {} is {}.".format(list2, sum_list2))