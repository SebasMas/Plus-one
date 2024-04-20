class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if len(digits) <= 1 and digits[0] + 1 <= 9 :
            digits[0] += 1 
            return digits
        elif len(digits) > 1:
            digits[-1] += 1
            return digits
        else:
            digits[0] += 1
            newDigits = [int(number) for number in str(digits[0])]
            return newDigits
                
numbers = [9,9]
s = Solution()
print(s.plusOne(numbers))

            
                