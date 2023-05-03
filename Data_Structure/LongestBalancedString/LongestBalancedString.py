from collections import deque

def solve(A):
	charLst = deque([])
	cnt = [0, 0]
	for i in A:
		if i == '1':
			cnt[1] += 1
		elif i == '0':
			cnt[0] += 1
		charLst.append(int(i))
		
	if cnt[0] > cnt[1]:
		m, n = 0, 1
	else:
		m, n = 1, 0

	while cnt[0] != cnt[1]:
		if charLst[0] == m:
			charLst.popleft()
			cnt[m] -= 1
		elif charLst[-1] == m:
			charLst.pop()
			cnt[m] -= 1
		else: # front, back 모두 n인 경우 ?
			charLst.pop()
			cnt[n] -= 1
			
			
	return len(charLst)
    
	
	
	
A = input().strip()
print(solve(A))

# 0과 1의 개수를 모두 센다
# 0, 1중 개수가 적은 수가 n개라고 하자
# if string에 0, 1중 개수가 많은 수의 뭉치가 n보다 길게 있지 않다면
# 0과 1이 각각 n개씩 있는 문자열이 가장 긴 balanced substring 일 것이다
# else string에 0, 1중 개수가 많은 수의 뭉치가 n보다 길게 있다면
# 해당 뭉치를 기준으로 문자열을 자른 후
# 0, 1중 개수가 적은 수가 더 많이 있는 쪽에서 더 긴 balanced substring이 나올 것이다
# -> 보류

# ! 길이를 출력하는 것이기 때문에 조금 더 간결한 알고리즘이 있을 것 같은데?

# string을 dequeue에 저장
# dequeue 안에 0, 1의 개수를 계속해서 count
# 두개의 값이 같아질 때까지 pop_front or pop_left 반복
# 두개의 값이 같아지면 dequeue의 크기 출력

# 설계
# 0, 1중 dequeue 안에 더 많이 있는 수를 m, 나머지 한 수를 n 이라 하자
# if dequeue의 fornt, back 중에 m이 있다면 ? m을 pop
# elif dequeue의 front, back에 모두 n이 있다면 ? 무조건 pop_back을 해서 나온 결과와 pop_front을 해서 나온 결과를 비교한다
# elif dequeue의 front, back에 모두 m 이 있다면 ? 둘 중 아무거나 pop해도 된다
# dequeue 안에 0, 1의 개수가 같아지면 dequeue의 길이 출력


# ##

# what if same line changed?

