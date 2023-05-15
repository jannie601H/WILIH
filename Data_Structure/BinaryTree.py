def preorder(v): # return visited sequence of v by preorder
    # preorder: 탐색할 때 print
    # 방문하는 것이 아닌 counting 해야함으로 비재귀 DFS 구현?
    curr = root
    cnt = 1
    stack = [] # need to visit -> stack에 right left 순으로 넣고 다음 방문

    while curr != v:
        cnt += 1
        if right[curr] != 0:
            stack.append(right[curr])
        if left[curr] != 0:
            stack.append(left[curr])
        if stack:
            curr = stack.pop()
        else: # visited all nodes
            break
        
    return cnt

def postorder(v): # return visited sequence of v by postorder
    # postorder: left, right 다찍고 print
    curr = root
    cnt = 0
    stack = [] # need to visit -> stack에 right left 순으로 넣고 다음 방문
    visited = [] # visited node

    while True:
        stack.append(curr) # 한번 방문한 노드 left right 모두 방문한 후 다시 방문
        visited.append(curr)
        if right[curr] != 0:
            stack.append(right[curr])
        if left[curr] != 0:
            stack.append(left[curr])
        if stack:
            curr = stack.pop()
            while curr in visited: # if curr is visited once, count
                cnt += 1
                if curr == v: # node v counted
                    return cnt
                if stack:
                    curr = stack.pop()
        if not stack: # visited all nodes
            break

def depth(v): # return depth of v
    dep = 0
    while parent[v] != 0: # follow parent until parent is root
        v = parent[v]
        dep += 1

    return dep

def is_ancestor(u, v): # if u is ancestor of v -> return True / else return False
    curr = v
    while parent[curr] != 0:
        if curr == u:
            return True
        curr = parent[curr]
    return False
    

def lca(u, v):
    uDep = depth(u)
    vDep = depth(v)
    if vDep > uDep: # u is same or lower than v
        u, v = v, u
        uDep, vDep = vDep, uDep
    while uDep > vDep: # make u, v at same height
        u = parent[u]
        uDep -= 1
    while u != v:
        u = parent[u]
        v = parent[v]
    return u
    

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