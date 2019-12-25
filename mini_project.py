class Node:
	def __init__(self,value):
		self.right = None
		self.left = None
		self.center = value
#Insertion 
	def insert(self,value):
		if self.center:
			if value<self.center:
				if self.left is None:
					self.left = Node(value)
				else:
					self.left.insert(value)
			elif value>self.center:
				if self.right is None:
					self.right = Node(value)
				else:
					self.right.insert(value)
			else:
				self.center = value

	def inorder(self,tree):
		listx=[]
		if tree:
			listx = self.inorder(tree.left)
			listx.append(tree.center)
			listx = listx+self.inorder(tree.right)
		return listx

	def preorder(self,tree):
		listy=[]
		if tree:
			listy.append(tree.center)
			listy = listy+self.preorder(tree.left)
			listy = listy+self.preorder(tree.right)
		return listy

	def postorder(self,tree):
		listz=[]
		if tree:
			listz = self.postorder(tree.left)
			listz = listz + self.postorder(tree.right)
			listz.append(tree.center)
		return listz
        



a = input("Create a Root::")
root = Node(int(a))

n = input("How many data do you want to insert?::")
for x in range(0,int(n)):
	x = input("Data::")
	root.insert(int(x))

print("preorder:")
print(root.preorder(root))

print("postorder:")
print(root.postorder(root))

print("inorder:")
print(root.inorder(root))