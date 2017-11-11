

def NumDecodingWays(numString):

    if numString.__len__() == 0:
        return 0

    currWays = 1
    prevWays = 0

    currTempWay = 0

    prevDigit = None

    for index, currDigit in enumerate(numString):

        if index == 0:
            if currDigit != '0':
                currTempWay = 1
            else:
                return 0
            prevDigit = currDigit
            prevWays = currWays
            currWays = currTempWay

        else:
            currTempWay = 0
            if currDigit != '0':
                currTempWay = currWays

            if prevDigit != '0':
                # take 2 digit prevDigit and currDigit
                num = (int(str(prevDigit) + str(currDigit)))
                if num >= 10 and num <=26:
                    currTempWay += prevWays

            prevWays = currWays
            currWays = currTempWay
            prevDigit = currDigit

    return currWays


if __name__ == "__main__":

    x = input("Enter the encoded message: ")
    n = NumDecodingWays(x)

    print(str(n))