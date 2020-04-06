#a self dividing number is a number that can be divided by all the numbers it contains
#128 is self dividing because it is divisible by 1,2, and 8
# given a lower bound and an upper bound return a list of all the
# self dividing numbers within those bounds
#the bounds will not include negative numbers or 0? 
#I am going assume negatives are left out for now. 
#The input bounds will be correct.
# eg. the upper bound will not be lower than the lower bound.
#I will assume so.


def self_dividing_numbers(lower: int, upper: int):
    list_of_answers = []
    self_dividing = False
    for num in range(lower, upper + 1):
        num_as_string = str(num)
        for char in num_as_string:
            if char == '0':
                self_dividing = False
                break
            elif num % int(char) == 0:
                self_dividing = True
            else:
                self_dividing = False
                break
        if(self_dividing == True):   
            list_of_answers.append(num)
        
    return list_of_answers

        


if __name__ == "__main__":


    list_of_nums = self_dividing_numbers(1, 22)
    print(list_of_nums)



