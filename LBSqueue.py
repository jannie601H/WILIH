from collections import deque
import sys
input = sys.stdin.readline

def solve(A):
    queue = deque([])
    strLst = deque(list(map(int, A.strip())))
    scnt = [strLst.count(0), strLst.count(1)] # s 안에 0, 1 개수

    # m: 개수가 더 많은 수, n: 개수가 더 적은 수
    if scnt[0] > scnt[1]:
        m, n = 0, 1
    if scnt[0] < scnt[1]:
        m, n = 1, 0
    if scnt[0] == scnt[1]:
        return len(strLst)

    qcnt = [0, 0] # q 안에 0, 1 개수
    maxLen = 0
    for i in strLst: 
        # q 안에 값을 하나씩 넣어주면서 0, 1개수 count
        queue.append(i)
        qcnt[i] += 1

        while qcnt[m] > scnt[n]: #or qcnt[m] > qcnt[n]: # q안에 m의 개수가 s안에 n의 개수보다 많아지면 bs 불가 (앞으로 q안에 들어갈 수 있는 n의 개수) # 해당 while문 O(1)
            # instm = qcnt[m]
            # instn = qcnt[n]
            # stack = deque([])
            # if queue[0] == n:
            #     while instm > instn:
            #         dequeued = queue.pop()
            #         if dequeued == n:
            #             instn -= 1
            #         elif dequeued == m:
            #             instm -= 1
            #         stack.append(dequeued)
            # if instm == instn:
            #     maxLen = max(maxLen, instm + instn)

            # for i in range(len(stack)):
            #     queue.append(stack.pop())
            
            dequeued = queue.popleft() # dequeue
            if dequeued == n: # n 이 dequeue 됐으면 q 안에 m이 scnt[n] - 1 보다 커지면 bs 불가함
                scnt[n] -= 1
                qcnt[n] -= 1
            elif dequeued == m:
                qcnt[m] -= 1

        # if qcnt[n] * 2 > maxLen: # 0111011101110 fail result 4 expected 2 (0이 q에 두개들어가는 순간이 생긴다)
        #     maxLen = qcnt[n] * 2
        
        # for j in range(len(queue) - 2*qcnt[n] + 1):
        #     inst = queue[j : 2*qcnt[n]+j]
        #     cnt0, cnt1 = 0, 0
        #     for x in inst:
        #         if x == 0:
        #             cnt0 += 1
        #         elif x == 1:
        #             cnt1 += 1
        #     if cnt0 == cnt1:
        #         if len(inst) > maxLen:
        #             maxLen = len(inst)
        # print('outside',queue)
        if qcnt[m] == qcnt[n]: # q안에 0, 1의 개수가 같아지면 maxLen update
            maxLen = max(maxLen, len(queue)) # 111100011111100 fail -> result 4 expected 6 (1 4개가 먼저 나오고 0 3개가 들어가서 개수가 같아지는 순간이 오지 않는다)

        if qcnt[m] > qcnt[n] and (queue[0] or queue[-1] == m) and qcnt[n] > maxLen/2:
            stack = deque([])
            while qcnt[m] > qcnt[n] and (queue[0] or queue[-1] == m):
                if queue[0] == m:
                    stack.append(['l', queue.popleft()])
                    qcnt[m] -= 1
                elif queue[-1] == m:
                    stack.append(['r', queue.pop()])
                    qcnt[m] -= 1

                # print("inside",queue)
                if qcnt[m] == qcnt[n]:
                    maxLen = max(maxLen, qcnt[m]*2)
            for _ in range(len(stack)):
                flag = stack.pop()
                if flag[0] == 'l':
                    queue.appendleft(flag[1])
                    qcnt[flag[1]] += 1
                if flag[1] == 'r':
                    queue.append(flag[1])
                    qcnt[flag[1]] += 1
                # print('recover', queue)

        
        # if qcnt[m] > qcnt[n]: # 예외처리
        #     inst = queue.copy()
        #     instm, instn = qcnt[m], qcnt[n]
        #     while instm != instn:
        #         if len(inst) == 0:
        #             break
        #         flag = inst.popleft()
        #         if flag == m:
        #             instm -= 1
        #         if flag == n:
        #             instn -= 1
        #     maxLen = max(maxLen, len(inst))
                

    return maxLen

A = input().strip()
print(solve(A))