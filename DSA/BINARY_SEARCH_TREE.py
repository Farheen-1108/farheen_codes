class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    # insertions:
    def insert (self,root,key):
        if root is None:
            return node(key)         
        if key < root.key:
            root.left = self.insert(root.left, key)          #recurssive calling function
        else:
            root.right = self.insert(root.right, key)
        return root
    
# inorder tranversal (sorted order)                      (left, root , right --- inorder)
    def inorder (self,root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)
# search
    def search (self,root,key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left , key)
        return self.search(root.right , key)
    

# find the minimum value node:                   in deletion case 3 " when there is only two childrens
    def minValuenode(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# deletion:
    def delete(self,root,key): 
        if root is None:
            return root
        if key < root.key: 
            root.left = self.delete(root.left, key)             # recurssive
        elif key > root.key:
            root.right = self.delete(root.right , key)           # recurssive
        else:
            #node with one child or no chlid
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.right
            #node with two children
            temp = self.minValuenode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root 
#-- test the bst implementation:
tree = BST()
keys = [50, 30 , 70 , 20, 40, 60, 80]

for key in keys:
    tree.root = tree.insert (tree.root , key)

print("Inorder traversal of the BST")
tree.inorder(tree.root)

# search for the a key:
key = 60
found = tree.search(tree.root, key)
print(f"\n\nSearch for {key}:", "Found" if found else "Not Found")
print(f"\nSearch for {key}:", "Found" if found else "Not Found")

# Delete A node:

tree.root = tree.delete(tree.root, 20)
print("\nInorder after deleting 20:")
tree.inorder(tree.root)

tree.root = tree.delete(tree.root, 30)
print("\nInorder after deleting 30:")
tree.inorder(tree.root)

tree.root = tree.delete(tree.root, 50)
print("\nInorder after deleting 50:")
tree.inorder(tree.root)

