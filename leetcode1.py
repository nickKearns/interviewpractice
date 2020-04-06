
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