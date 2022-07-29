import sys
sys.stdin = open('_직사각형길이찾기.txt')

t = int(input())                                     # 케이스 수 입력

for i in range(t):                                   # 케이스 반복
    num_lst = list(map(int,input().split()))         # 입력 받은 숫자들을 리스트에 저장
    num_dic = dict()                                 # 길이와 횟수 저장을 위해 딕셔너리 선언

    for number in num_lst:                           # 데이터에서 숫자를 순서대로 가져옴
        if number in num_dic:                        # 가져온 숫자가 딕셔너리에 있는지
            num_dic[number] += 1                     # 있다면 value를 +1
        else:                                        # 없다면
            num_dic[number] = 1                      # 키와 값 추가

    for key in num_dic:                              # 딕셔너리에서 키 가져옴
        if num_dic[key] == 1 or num_dic[key] == 3:   # 값이 1 또는 3이면 길이로 키를 출력
            print(f'#{i+1} {key}')