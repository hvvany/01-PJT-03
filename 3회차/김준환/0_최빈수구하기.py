import sys
sys.stdin = open("_최빈수구하기.txt")

n = int(input())                               # 전체 케이스 수 입력

for i in range(n):                             # 케이스 반복
    score=[]                                   # 점수 종류 저장
    count=[]                                   # 점수 종류별 개수 저장
    case_num = input()                         # 케이스 번호를 입력 받기
    score_lst = list(map(int,input().split())) # 입력 받은 모든 점수를 리스트에 담기
    score_lst.sort()                           # 점수 리스트 순서대로 정렬

    for sc in score_lst:                       # 모든 점수를 저장한 리스트에서 점수를 가져옴
        if sc not in score:                    # 가져온 점수가 종류 리스트에 없으면
            score.append(sc)                   # 점수 종류 리스트에 추가
            count.append(1)                    # 개수 리스트에 같은 인덱스에 초기값 1 입력
        else:                                  # 가져온 점수가 이미 리스트에 있을때
            count[score.index(sc)] += 1        # 해당 점수 종류의 인덱스와 같은 인덱스의 
                                               # count리스트에 1을 더하기
    cnt = 0                                    
    for i in range(len(count)):                # count리스트 또는 score리스트의 길이만큼 반복하며 인덱스 접근
        second_cnt = count[i]                  # 두 번째 카운트는 현재 불러온 count리스트의 값
        if second_cnt >= cnt:                  # 현재 값이 이전에 최대값 보다 크거나 같을때
            cnt = count[i]                     # cnt 값을 현재 값으로 최신화
            answer = score[i]                  # answer변수에는 현재 인덱스의 score값 저장
    print(f'#{case_num} {answer}')             