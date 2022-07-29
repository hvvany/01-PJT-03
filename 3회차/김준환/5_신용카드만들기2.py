import sys
sys.stdin = open('_신용카드만들기2.txt')

t = int(input())                                            # 케이스 개수

for i in range(t):                                          # 케이스 반복
    number_lst = list(map(str, input()))                    # 데이터를 리스트에 저장
    
    idx=0                                      
    for number in number_lst:                               # 저장한 리스트에서 문자 하나씩 가져오기
        if number == '-':                                   # 가져온 값이 - 이면 
            number_lst.pop(idx)                             # 삭제[idx인덱스]
        idx += 1                                            # 인덱스 +1

    if number_lst[0] in '34569' and len(number_lst) == 16:  # 앞 숫자가 34569중에 하나이고 길이가 16이면
        answer = 1                                          # 1 출력
    else:                                   
        answer = 0                                          # 아니면 0 출력
    print(f'#{i+1} {answer}')