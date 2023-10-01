
def romanToInt(s):
    Roman_nums = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
    num = 0
    y = 0
    while y < len(s):
        num_1 = Roman_nums[s[y]]
        if y + 1 < len(s):
            num_2 = Roman_nums[s[y + 1]]
            if num_1 == num_2 or num_1 > num_2:
                num += num_1
                y += 1
                continue
            if num_1 < num_2:
                num += num_2 - num_1
                y += 2
                continue
        else:
            if len(s) > y:
                previous_num = Roman_nums[s[y - 1]]
                if num_1 == previous_num or num_1 < previous_num:
                    num += num_1
        y = y + 1
    return num

print(romanToInt("DCXXI"))