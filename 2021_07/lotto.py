def solution(lottos, win_nums):
    best_nums = 0
    worst_nums = 0
    nums = 0
    zeros = lottos.count(0)
    for i in lottos:
        if i in win_nums:          
            nums += 1
    best_nums = nums + zeros
    worst_nums = nums
                
    best = {6:1, 5:2, 4:3, 3:4, 2:5}.get(best_nums, 6)
    worst = {6:1, 5:2, 4:3, 3:4, 2:5}.get(worst_nums, 6)
    result = [best, worst]
    return result
