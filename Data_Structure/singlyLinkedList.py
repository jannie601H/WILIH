class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		node = Node(key)
		node.next = self.head
		self.head = node
		self.size += 1

	def pushBack(self, key):
		tail = self.head
		while tail.next != None:
			tail = tail.next
		tail.next = Node(key)
		self.size += 1

	def popFront(self):
		if self.head == None:
			return None
		popKey = self.head.key
		self.head = self.head.next
		self.size -= 1
		return popKey
		# head 노드의 값 리턴. empty list이면 None 리턴

	def popBack(self):
		if self.head == None:
			return None
		tail = self.head
		bhead = None
		while tail.next != None:
			bhead = tail
			tail = tail.next
		if bhead == None:
			popKey = tail.key
			self.head = None
			self.size -= 1
			return popKey
		else:
			popKey = tail.key
			bhead.next = None
			self.size -= 1
			return popKey
		# tail 노드의 값 리턴. empty list이면 None 리턴

	def search(self, key):
		curr = self.head
		while curr != None:
			if curr.key == key:
				return curr
			curr = curr.next
		return curr
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		
	def remove(self, x):
		self.size -= 1
		curr = self.head
		bhead = None
		while curr != None:
			if curr == x and bhead == None:
				self.head = curr.next
				return True
			elif curr == x:
				bhead.next = curr.next
				return True
			bhead = curr
			curr = curr.next
		self.size += 1
		return False
				
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")