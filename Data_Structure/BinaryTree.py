def preorder(v):
    

def postorder(v):
    

def depth(v): # return depth of v
    dep = 0
    while parent[v] != None: # follow parent until parent is root
        v = parent[v]
        dep += 1

    return dep

def is_ancestor(u, v): # if u is ancestor of v -> return True / else return False
    

def lca(u, v):
    

# 입력 처리 부분 (여기에)
n = int(input())
parent = [None] * n
left = [None] * n
right = [None] * n

for _ in range(n):
    v, l, r = tuple(map(int, input()))
    left[v] = l
    right[v] = r
    # how do i find parent of v?
    p = None # instant parent node
    # update parent node of v if any node has v as a child
    for i in left:
        if i == v:
            p = i
    for i in right:
        if i == v:
            p = i

    if p == None:
        root = v # if p == None, v is root!
    parent[v] = p




# 전처리 코드 부분 (여기에)

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