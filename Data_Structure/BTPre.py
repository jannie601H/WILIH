def preorder(v):
	return pre[v-1]

def postorder(v):
	return post[v-1]

def depth(v):
	return depth_pre[v - 1]

def is_ancestor(u, v):
	if u == v:
		return True
	while parent[v-1] != 0:
		v = parent[v-1]
		if u == v:
			return True
	return False

def lca(u, v):
	while u != v:
		if depth(u) > depth(v):
			u = parent[u-1]
		else:
			v = parent[v-1]
	return v
		

# 입력 처리 부분 (여기에)
n = int(input())
left = [0] * n
right = [0] * n
parent = [0] * n
root = None
for i in range(n):
	numbers = [int(i) for i in input().split()]
	left[numbers[0] - 1] = numbers[1]
	right[numbers[0] - 1] = numbers[2]
	if numbers[1]:
		parent[numbers[1] - 1] = numbers[0]
	if numbers[2]:
		parent[numbers[2] - 1] = numbers[0]
	

# 전처리 코드 부분 (여기에)
# 전처리를 통해 Preorder, Postorder list를 생성한다.
root = [i + 1 for i in range(len(parent)) if parent[i] == 0][0]
pre = [0] * n
post = [0] * n
depth_pre = [0] * n
t1 = t2 = 1
def preprocessing(v):
	global t1, t2
	if v:
		pre[v - 1] = t1
		t1 += 1
		if parent[v-1]:
			depth_pre[v-1] = depth_pre[parent[v-1] - 1] + 1
		preprocessing(left[v-1])
		preprocessing(right[v-1])
		post[v - 1] = t2
		t2 += 1
		
preprocessing(root)


# 
# 명령 처리 부분으로 아래는 수정 하지 말 것!
#
while True:
    cmd = input().split()
    if cmd[0] == 'exit':
        break
    elif cmd[0] == 'preorder':
        res = preorder(int(cmd[1]))
        print(f"  > preorder({int(cmd[1])}) = {res}")
    elif cmd[0] == 'postorder':
        res = postorder(int(cmd[1]))
        print(f"  > postorder({int(cmd[1])}) = {res}")
    elif cmd[0] == 'depth':
        res = depth(int(cmd[1]))
        print(f"  > depth({int(cmd[1])}) = {res}")
    elif cmd[0] == 'is_ancestor':
        res = is_ancestor(int(cmd[1]), int(cmd[2]))
        print(f"  > {int(cmd[1])} is {'an' if res else 'not an'} ancestor of {int(cmd[2])}")
    elif cmd[0] == 'lca':
        res = lca(int(cmd[1]), int(cmd[2]))
        print(f"  > lca({int(cmd[1])}, {int(cmd[2])}) = {res}")
    else:
        print("illegal command")