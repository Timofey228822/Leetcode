class Solution(object):
    def romanToInt(self, s):
        Roman_nums = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
            }
        num = ''
        r2 = ['I','V','X','L','C','D','M']

        for i in range(0, len(list(s)) - 1):
            if Roman_nums[r2[i]] > Roman_nums[r2[i + 1]] or Roman_nums[r2[i]] == Roman_nums[r2[i + 1]]:
                num = num + str(Roman_nums[r2[i]] + Roman_nums[r2[i+1]])
            else:
                num = num + str(Roman_nums[r2[i + 1]] - Roman_nums[r2[i]])
        return int(num)