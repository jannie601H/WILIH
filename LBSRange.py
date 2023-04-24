from collections import deque
import sys
input = sys.stdin.readline

def solve(A):
    queue = []
    strLst = []
    scnt = [0, 0] # s 안에 0, 1 개수
    for c in A: #O(n)
        if c == '0':
            scnt[0] += 1
        elif c == '1':
            scnt[1] += 1
        strLst.append(int(c))

    # m: 개수가 더 많은 수, n: 개수가 더 적은 수
    if scnt[0] > scnt[1]:
        m, n = 0, 1
    if scnt[0] < scnt[1]:
        m, n = 1, 0
    if scnt[0] == scnt[1]:
        return len(strLst)
    
    # range = scnt[n] * 2 짜리 구간을 모두 잡아보고 안나오면 range -= 1 구간 잡아보기 반복
    psbRange = scnt[n] * 2
    while psbRange > 0:
        for i in range(len(strLst) - psbRange + 1):
            inst = strLst[i:i+psbRange]
            if inst.count(1) == inst.count(0):
                return psbRange

        psbRange -= 1
    return psbRange

A = input().strip()
print(solve(A))