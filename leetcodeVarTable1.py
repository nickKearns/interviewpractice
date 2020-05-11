#given a non negative integer return the number of steps to reduce it to zero
#if the number is even divide by 2 if it is odd subtract 1

#might be able to do this with recursion

#    num        steps
#    14         0
#    7          1
#    6          2
#    3          3
#    2          4
#    1          5
#    0          6



#this is an interesting test case because it alternates from even to odd the entire way until 0

#that does not always happen
#I thought maybe there could be a way to 


def number_of_steps(num, num_steps=0):
    if num == 0:
        return num_steps
    elif num % 2 == 0:
        return number_of_steps(num / 2, num_steps + 1)
    else:
        return number_of_steps(num - 1, num_steps + 1)



if __name__ == "__main__":
    print(number_of_steps(123))
