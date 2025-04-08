# def slice_array(arr, start, end):
#     return arr[start:end]

#     arr = [1, 2, 3, 4, 5]
#     result = slice_array(arr, 1, 3)
# print(result)

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

    numbers = [1, 2, 3, 4, 5]
    num1 = 1
    num2 = 3
    print(solution(numbers, num1, num2))