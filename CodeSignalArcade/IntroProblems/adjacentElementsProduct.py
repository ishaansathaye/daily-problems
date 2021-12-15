#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

#original
def solution(inputArray):
    max_product = -1001
    for i in range(len(inputArray)):
        prev = max_product
        if i != len(inputArray)-1:
            product = inputArray[i]*inputArray[i+1]
        if product > prev:
            max_product = product
    return max_product

#concise solution
def solution2(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

inputArray = [3, 6, -2, -5, 7, 3]
print(solution(inputArray))
print(solution2(inputArray))