#given an array and a target value find two numbers that sum to the target value
#what if there are more than 1 combination of numbers that add up to the target
#return the first found combo
#assume the list is not ordered
#[1,5,8,4,10] -> 12
#store all the complements in a dictionary and then with each 
#iteration over the list check if that number exists in the built dictionary


def find_target(arr, target):
    seen_comps = {}
    for num in arr:
        complement = target - num
        if complement in seen_comps:
            seen_comps[complement] += 1
            return (complement, num)
        else:
            seen_comps[num] = 1


if __name__ == "__main__":

    test_list = [1,5,8,4,10]
    print(find_target(test_list, 12))
