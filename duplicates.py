#given a list of n numbers determine if it includes any duplicate numbers
#Does a duplicate number mean it appears more than once or exactly twice?
#I am going to assume it means any number that is repeated more than once
#The question asked to determine if it includes any duplicates so I will return a boolean



def find_duplicates(num_arr):
    dict = {}
    for num in num_arr:
        if num in dict:
            return True
        else:
            dict[num] = 1
    return False


if __name__ == "__main__":
    test_arr = [1,2,3,4,5,6,7,8]
    print(find_duplicates(test_arr))
