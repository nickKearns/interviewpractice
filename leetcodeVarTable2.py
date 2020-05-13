#given an array, called candies, and an integer, called extraCandies. 
#candies[i] is the number of candies the Ith kid has
#for every kid check if there is a way to distribute extraCandies among the kids such that he or she can have
#the greatest number of candies among them. Multiple kids can have the greatest number of candies
#what should the output of the function be?
#output should be an array of booleans, being whether that kid in the array
#could have the greatest number of candies



#var table


#candies = [2,3,5,1,3]
#extra candies = 3

#           
#       
#       kid         # of candies        max number it could be          current max # of candies            result
#       0               2                          5                                5                         true
#       1               3                           6                               5                         true
#       2               5                           10                              5                         true
#       3               1                           4                               5                         false
#       4               3                           6                               5                         true

#output would be [true, true, true, false, true]


#i need to find the greatest number of candies

def kidsWithCandies(candies, extra_candies):

    greatest_num_candies = candies[0]
    result_arr = []

    #finding the greatest num of candies
    for num_candy in candies:
        if num_candy > greatest_num_candies:
            greatest_num_candies = num_candy

    for num_candy_for_kid in candies:
        if num_candy_for_kid + extra_candies >= greatest_num_candies:
            result_arr.append(True)
        else:
            result_arr.append(False)

    return result_arr



if __name__ == "__main__":
    candies_arr = [2,3,5,1,3]

    result = kidsWithCandies(candies_arr, 3)
    print(result)

