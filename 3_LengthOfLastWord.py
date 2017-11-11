
def lengthOfLastWord(s):

    x = s.__len__()
    if s.__len__() == 0:
        return 0



    wordStartIndex = None
    count = 0

    #run from last letter to first character to find the first starting letter from the last. We need to exclude the spaces at last.
    for index in range(s.__len__()-1, -1, -1):
        if s[index] != ' ':
            wordStartIndex = index
            break

    #If we didnt find the letter in the string. Then rewturn count = 0
    if wordStartIndex == None:
        return count

    #If we find the letter then count the number of characters in the word
    for index in range(wordStartIndex, -1,-1):
        if s[index] == ' ':
            break
        count +=1


    return count


if __name__ == "__main__":
    n = lengthOfLastWord(input("Enter the String: "))

    print("Length of last word is = " + str(n))
