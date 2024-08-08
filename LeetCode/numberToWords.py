class Solution:
    def __init__(self):
        # dummy string in the front to match indices
        self.below20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                        "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen",
                        "Fifteen", "Sixteen",
                        "Seventeen", "Eighteen", "Nineteen",]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty",
                     "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        '''O(1) TC'''
        if num == 0:
            return "Zero"
        res = ""
        i = 0  # idx on thousands
        while num > 0:
            triplet = num % 1000
            if triplet != 0:
                # only triplet then i == 0
                res = self.helper(triplet).strip() + " " + \
                    self.thousands[i] + " " + res
            i += 1
            # get only thousands
            num = num//1000

        return res.strip()

    def helper(self, num):
        if num < 20:
            return self.below20[num]
        elif num < 100:
            return self.tens[num//10] + " " + self.helper(num % 10)
        else:
            return self.below20[num//100]
            + " Hundred " + self.helper(num % 100)
