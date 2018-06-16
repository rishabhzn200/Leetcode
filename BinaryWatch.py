"""
401. Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the
watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        hrMinList = []
        includeExclude = []
        mapping = {1:1, 2:2, 3:4, 4:8, 5:1, 6:2, 7:4, 8:8, 9:16, 10:32}


        def mapHrAndMin(mapLen, start, end, target, incExc):



            if start == end:
                numLightsOn = sum(1 for y in incExc if y == 1)
                if numLightsOn == target:
                    hr = 0
                    min = 0
                    for index in range(len(incExc)):
                        if incExc[index] == 1:
                            if (index+1) <=4:
                                hr += mapping[index+1]
                            else:
                                min += mapping[index+1]

                    if min < 10:
                        min = str('0')+str(min)
                    time = str(hr) + ":" + str(min)
                    hrMinList.append(time)

                return

                pass

            for j in range(0,2):
                incExc.append(j)
                mapHrAndMin(mapLen, start+1, end, target, incExc)
                del incExc[-1]

            pass

        mapHrAndMin(len(mapping.keys()), 0, len(mapping.keys()), num, includeExclude)
        return hrMinList


print(Solution().readBinaryWatch(2))


list1 = ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
list2 = ['0:48', '0:40', '0:24', '0:36', '0:20', '0:12', '0:34', '0:18', '0:10', '0:06', '0:33', '0:17', '0:09', '0:05', '0:03', '8:32', '8:16', '8:08', '8:04', '8:02', '8:01', '4:32', '4:16', '4:08', '4:04', '4:02', '4:01', '12:00', '2:32', '2:16', '2:08', '2:04', '2:02', '2:01', '10:00', '6:00', '1:32', '1:16', '1:08', '1:04', '1:02', '1:01', '9:00', '5:00', '3:00']

for i in list2:
    if i not in list1:
        print(i)

for i in list1:
    if i not in list2:
        print(i)