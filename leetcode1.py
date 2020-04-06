#I am given two arrays that are strings, the first array is identifying 
#which stones are jewels
#the second array is the stones I am given
#I am to return how many jewels I have in the second array 
#letters are case sensitive
#all characters in the arrays are letters



def numJewelsInStones(J, S):
    num_jewels = 0
    for i in range(len(S)):
        if S[i] in J:
            num_jewels += 1
    return num_jewels


if __name__ == "__main__":

    jewels = "aA"
    stones = "aAAbbbb"

    numb_jewels = numJewelsInStones(jewels, stones)
    print(numb_jewels)