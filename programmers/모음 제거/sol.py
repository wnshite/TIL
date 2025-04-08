# 1번 방법
def solution(my_string):
    collection = ("a", "e", "i", "o", "u")
    answer = ""

    for i in my_string:
        if i not in collection:
            answer += i
    return answer

# 2번 방법
def solution(my_string):
    collection = ("a", "e", "i", "o", "u")
    
    for i in collection:
        my_string = my_string.replace(i, "")
    return my_string