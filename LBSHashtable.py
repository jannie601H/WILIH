import sys
input = sys.stdin.readline

def solve(A):
    hashTable = {0:-1} # 첫 시작 0으로 초기화
    strLst = list(map(int, A.strip()))
    binarySum = 0
    result = 0

    for i, val in enumerate(strLst):
        if val == 0:
            binarySum -= 1
        if val == 1:
            binarySum += 1
        
        if binarySum not in hashTable: # hashTable에 key가 없다면 현재 index를 value로 key 생성
            hashTable[binarySum] = i
        if binarySum in hashTable: # hashTable에 key가 있으면 부분부문자열 존재! -> 현재 index - 해당 key의 value값(최초 key 등장 index) 까지가 부분부문자열
            result = max(result, i - hashTable[binarySum]) # 최대길이 update
        
    return result

A = input().strip()
print(solve(A))

# idea
# 문자열 앞에서부터 읽는다
# 1이나오면 sum에 +1 0이나오면 -1
# 증가하다 감소 or 감소하다 증가하는 부분이 있으면 균형부문자열 존재함
# 그중 가장 긴 것을 찾아야 한다
# 해쉬테이블을 이용해서 sum값이 최초로 나온 index를 저장해두면
# 다시 똑같은 sum값이 나왔을 때 index까지가 균형부문자열
# 찾아진 균형부문자열 중 가장 긴 값 출력