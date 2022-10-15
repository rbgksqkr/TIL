from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    left = bisect_left(array, left_value)
    right = bisect_right(array, right_value)
    return right - left

def solution(words, queries):
    len_word = [[] for _ in range(10001)] # 가사 단어의 길이 별로 나누기
    reversed_len_word = [[] for _ in range(10001)] # 정렬해야되서 ?가 앞에 나오는 경우 분리
    answer = [0] * (len(queries))
    for word in words:
        len_word[len(word)].append(word)
        reversed_len_word[len(word)].append(word[::-1])
    
    for i in range(10001):
        len_word[i].sort()
        reversed_len_word[i].sort()
    
    # ex) fro??
    # 연속된 ?를 변환
    # froaa ~ frozz 사이에 있는 단어 개수 세기
    for i in range(len(queries)):
        if queries[i][0] != '?':
            answer[i] = count_by_range(len_word[len(queries[i])], queries[i].replace('?', 'a'), queries[i].replace('?', 'z'))
        else:
            answer[i] = count_by_range(reversed_len_word[len(queries[i])], queries[i][::-1].replace('?', 'a'), queries[i][::-1].replace('?', 'z'))
    return answer
            
            

