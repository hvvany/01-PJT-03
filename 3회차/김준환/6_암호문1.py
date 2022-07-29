import sys
sys.stdin = open('_암호문1.txt')

for number in range(10):                             # 전체 10개 케이스 반복
    l = int(input())                                 # 원본 암호문 길이 l
    raw_code_lst = list(input().split())             # 원본 암호문 리스트에 저장
    fix_cnt = int(input())                           # 명령어 개수
    fix_code_lst = list(input().split())             # 명령어 리스트에 저장

    def Fix_Code(i):                                 # I 의 인덱스 입력받아 코드 수정하는 함수
        idx = int(fix_code_lst[i+1])                 # 데이터를 추가할 위치의 인덱스
        long = int(fix_code_lst[i+2])                # 추가할 데이터의 길이
        for cod_lst in fix_code_lst[i+3:i+3+long]:   # 추가하고 싶은 데이터 구간을 잘라서 하나씩 불러옴
            raw_code_lst.insert(idx,cod_lst)         # 위에서 구한 인덱스 위치에 데이터 추가
            idx += 1                                 # 반복하며 순서대로 다음 인덱스에 데이터 추가
        return

    i = 0
    for case in fix_code_lst:           # 명령어 리스트에서 하나씩 불러옴
        if case == 'I':                 # 문자가 I이면 해당 인덱스를 함수로 넘김
            Fix_Code(i)
        i += 1

    print(f'#{number+1} ',end='')       # '#1' 같이 케이스 번호 출력
    for code in raw_code_lst[0:10]:     # 수정된 리스트에서 앞에 10개를 순서대로 불러와서
        print(code,end=' ')             # 프린트 문 안에서 붙여서 출력
    print('')                           # 개행
