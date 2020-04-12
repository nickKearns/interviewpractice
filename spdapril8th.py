#find the longest substring of unique letters within a string of n letters
#questions: does casing count as different letters?
#what if two substrings are of equal length and are the longest?
#Assume i can return the first substring, or either
#assume casing counts as different letters
#thinking of using a dictionary


#QUESTION 2 FOR HOMEWORK DUE APRIL 13TH


def find_substring(word):
    longest_substring = ''

    dict = {}
    for i in range(len(word)):

        counter = i
        built_substring = ''

        while word[counter] not in dict:

            dict[word[counter]] = 1
            
            built_substring += word[counter]

            if counter < len(word):
                counter += 1
            else:
                break

        if len(built_substring) > len(longest_substring):
            longest_substring = built_substring
    return longest_substring

if __name__ == "__main__":

    sample_str = 'ahgotnauhhtuyowl'
    print(find_substring(sample_str))




