def solution(dot):
    x, y = dot
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    
print(solution([2, 4]))
print(solution([-7, 9]))