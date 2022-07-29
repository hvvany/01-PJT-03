import sys
sys.stdin = open('_소득불균형.txt')

t = int(input())                                # 테스트 케이스 개수
for i in range(t):                              # 테스트 케이스 반복
    n = int(input())                            # 테스트 케이스에 리스트 길이
    money_lst = list(map(int,input().split()))  # 소득 리스트
    avg = sum(money_lst)/n                      # 평균
    cnt = 0                  
    for money in money_lst:                     # 소득 리스트에서 하나씩 가져옴
        if money <= avg:                        # 평균보다 작거나 같으면
            cnt += 1                            # 카운트 + 1
    print(f'#{i+1} {cnt}')                      # 평균보다 낮은 사람 수