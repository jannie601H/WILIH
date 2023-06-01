class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key): # key 값이 있다면 해당 Node return / 없다면 삽입될 곳의 부모노드 return
        curr = self.root
        parent = None
        while curr != None:
            if key == curr.key:
                return curr # key 값이 있으므로 해당 node return
            if key < curr.key:
                parent = curr
                curr = curr.left
            if key > curr.key:
                parent = curr
                curr = curr.right
        return parent # key 값이 없으므로 삽입될 곳의 부모노드 return

    def search(self, key): # key 값을 갖는 Node를 찾아 return 없다면 None return
        node = self.find_loc(key)
        if node.key == key:
            return node
        else:
            return None

    def insert(self, key):
        # 노드들의 height 정보 update 필요
        p = self.find_loc(key)
        
        if p == None or p.key != key:
            insert = Node(key)
            if p == None:
                self.root = insert
            else:
                if p.key > key:
                    p.left = insert
                if p.key < key:
                    p.right = insert
                insert.parent = p

        # height 정보 update
        parent = insert.parent
        curr_h = 0
        while curr_h == curr.height:
            curr.height += 1
            curr = curr.parent
            curr_h += 1

    def deleteByMerging(self, x):
        # 노드들의 height 정보 update 필요
        

    def deleteByCopying(self, x):
        # 노드들의 height 정보 update 필요

    def height(self, x): # 노드 x의 height 값을 리턴
        if x == None: return -1
        else: return x.height

    def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴

    def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴

    def rotateLeft(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)

    def rotateRight(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)

	
T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
