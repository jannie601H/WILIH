def cntPre(t, node):
    if node != 0:
        t += 1
        if left[node] != 0:
            t = cntPre(t, left[node])
        if right[node] != 0:
            t = cntPre(t, right[node])
    
    return t

def preorder(v): # return visited sequence of v by preorder
    # # preorder: 탐색할 때 print
    cnt = 1
    cur = root
    
    if cur != 0:
        cnt += 1
        if left[cur] != 0:
            cur = left[cur]
        if right[cur] != 0:
            cur = right[cur]

    return cnt

def postorder(v): # return visited sequence of v by postorder
    # postorder: left, right 다찍고 print
    cnt = 1
    cur = root
    
    if cur != 0:
        if left[cur] != 0:
            cur = left[cur]
        if right[cur] != 0:
            cur = right[cur]
        cnt += 1

    return cnt

def depth(v): # return depth of v
    dep = 0
    while parent[v] != 0: # follow parent until parent is root
        v = parent[v]
        dep += 1

    return dep

# def is_ancestor(u, v): # if u is ancestor of v -> return True / else return False
    

# def lca(u, v):
    

# 입력 처리 부분 (여기에)
n = int(input())
parent = [0] * (n+1)
left = [0] * (n+1)
right = [0] * (n+1)

for _ in range(n):
    v, l, r = tuple(map(int, input().split()))
    left[v] = l
    right[v] = r

# 전처리 코드 부분 (여기에)
for v in range(1, n+1): # available only if input data key is sequenced / else input v list needed
    p = 0 # instant parent node
    # update parent node of v if any node has v as a child
    for i, node in enumerate(left):
        if node == v:
            p = i
    for i, node in enumerate(right):
        if node == v:
            p = i

    if p == 0:
        root = v # if p == 0, v is root!
    parent[v] = p

# 
# 명령 처리 부분으로 아래는 수정 하지 말 것!
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