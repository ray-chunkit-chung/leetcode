MAX_NUM_ABS = '2147483647'
MIN_NUM_ABS = '2147483648'

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # unicode -> str
        s = s.encode()
        
        # clean whitespace
        s = s.lstrip()
        
        # return early for empty string
        if len(s) == 0:
            return 0
        
        # check sign
        is_positive = True
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            is_positive = False
            s = s[1:]
        
        # get numerics on the left only
        num = ''
        for i in s:
            if not i in '0123456789':
                break
            num += i
        num = num.lstrip('0')

        # return early for no digits
        if len(num) == 0:
            return 0

        # check within -2^31 < num < 2^31 - 1
        if is_positive and len(num) > len(MAX_NUM_ABS):
            num = MAX_NUM_ABS
        elif not is_positive and len(num) > len(MIN_NUM_ABS):
            num = MIN_NUM_ABS
        else:  
            num = num.zfill(len(MAX_NUM_ABS))
        
        # return case by case 
        if is_positive and num <= MAX_NUM_ABS:
            return int(num)
        
        elif is_positive and num > MAX_NUM_ABS:
            return int(MAX_NUM_ABS)
        
        elif not is_positive and num <= MIN_NUM_ABS:
            return -int(num) 
                
        elif not is_positive and num > MIN_NUM_ABS:
            return -int(MIN_NUM_ABS)

        else:
            return 'wtf??!!'
