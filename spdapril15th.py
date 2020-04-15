#given a string of n letters find the longest substring of unique letters
#does casing count as different letters?
#what should I return if two substrings of unique letters are equal
#return any of the the substrings 
#assume casing counts

#htielqogguipsadfoienqm
#dictionary, to keep track of the letters already seen


def find_substring(given_string):
    longest_substring = ''


    for i in range(len(given_string)):

        counter = i

        dict = {}

        built_substring = ''

        while given_string[counter] not in dict:

           

            dict[given_string[counter]] = 1
            built_substring += given_string[counter]


            if counter < len(given_string) - 1:
                counter += 1
            else:
                break



        if len(built_substring) > len(longest_substring):
            longest_substring = built_substring


    return longest_substring


if __name__ == "__main__":
    test_string = 'abcdefgghijklmnopqrs'
    print(find_substring(test_string))


