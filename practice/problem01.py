def max_score(scores):
    pass
    # 여기에 코드를 작성합니다.
    # max = scores[0]
    # for i in (1, len(scores)-1) :
    #     if max < scores[i] :
    #         max = scores[i]
    # return max

    max = 0
    for i in range(len(scores)):
        n = scores[i]
        if n > max:
            max = n
    return max
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
