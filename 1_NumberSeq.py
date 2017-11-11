

"""
Consider the count and say problem.
Eg.
1
11
21
1211
111221
The first term is read as “one” 1, which becomes the second term. The second term is read as
“two” 1, which becomes the third term. The third term is read as “one” 2 “one” 1, which
becomes the fourth term and so on.
Given an input ‘n’, generate the n-th term.
"""

def findNthTerm(n):
    term = "1"
    newTerm = ""
    if  n == 1:
        return term
    for i in range(1,n):
        #parse the string
        count = 0
        actualNum = None
        for index, char in enumerate(term):
            if index == 0:
                count = 1
                actualNum = char
            else:
                if char == term[index-1]:
                    count += 1
                else:
                    newTerm += str(count) + str(actualNum)
                    count = 1
                    actualNum = char

        if index == term.__len__()-1:
            newTerm += str(count) + str(actualNum)

        term = newTerm
        newTerm = ""
    return term


if __name__ == "__main__":
    nthTerm= findNthTerm(int(input("Enter the number: ")))
    print(nthTerm)
