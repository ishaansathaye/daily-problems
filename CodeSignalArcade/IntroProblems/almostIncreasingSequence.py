def solution(sequence):
    for i in range(len(sequence)):
        if sequence[i] > sequence[i+1]:
            sequence.remove(sequence[i+1])
            if sequence[i] > sequence[i+1]:
                return False
    return True

sequence = [1, 3, 2, 1] #False
sequence2 = [1, 3, 2] #True
print(solution(sequence2))