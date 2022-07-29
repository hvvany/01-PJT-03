import sys
sys.stdin = open('_문자열의거울상.txt')

t = int(input())                          # 케이스 개수 입력

before_lst = [ 'b' , 'q', 'p', 'd' ]      # 원래 문자 리스트
after_lst = [ 'd', 'p', 'q', 'b' ]        # 같은 인덱스에 변화된 문자 리스트
for i in range(t):                        # 케이스 수 반복
    test_lst = list(map(str,input()))     # test_lst에 입력값 저장
    answer = ''                           # 정답 초기값 문자열
    for text in test_lst:                 # 입력받은 문자 하나씩 가져오기
        idx = before_lst.index(text)      # 원래 문자 리스트에서 인덱스 찾기
        answer += after_lst[idx]          # 같은 인덱스의 변환 문자 aswer에 문자열 추가
    print(f'#{i+1} {answer[::-1]}')       # answer 문자열 거꾸로 출력