import sys
sys.stdin = open('_신용카드만들기1.txt')

t = int(input())                                        # 케이스 수 입력

for i in range(t):                                      # 케이스 반복
    num_lst = list(map(int,input().split()))            # 데이터를 리스트에 담기
    num_sum = sum(num_lst[1::2]) + sum(num_lst[0::2])*2 # 홀수는 2스텝씩 모두 더한 값에 2배 + 짝수 합
    first_num = num_sum%10                              # 1의 자리수를 first_num에 저장
    if first_num == 0:                                  # 1의 자리가 0이면 10으로 바꾸기
        first_num = 10
    print(f'#{i+1} {10-first_num}')                     # 10 - 일의자리수 출력