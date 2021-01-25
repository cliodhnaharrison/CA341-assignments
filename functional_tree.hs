-- Parametric data type to represent a binary tree
data Tree a =
  Null | Node a (Tree a) (Tree a)
  deriving (Read, Show)

-- Function to make a binary tree from a list
makeTree :: Ord a => [a] -> Tree a
makeTree [] = Null
makeTree [x] = Node x Null Null
makeTree (x:xs) = insert x (makeTree xs)

-- Function to insert a value into a binary tree
insert :: Ord a => a -> Tree a -> Tree a
insert x Null = Node x Null Null
insert x (Node n left right)
  | x == n = Node n left right
  | x < n = Node n (insert x left) right
  | x > n = Node n left (insert x right)

-- Function to find whether a value is in a binary tree
search :: Ord a => a -> Tree a -> Bool
search x Null = False
search x (Node n left right)
  | x == n = True
  | x < n = search x left
  | x > n = search x right

-- Function to return binary tree preorder traversal as a list
preorder :: Tree a -> [a]
preorder Null = []
preorder (Node x left right) = [x] ++ preorder left ++ preorder right

-- Function to return binary tree inorder traversal as a list
inorder :: Tree a -> [a]
inorder Null = []
inorder (Node x left right) = inorder left ++ [x] ++ inorder right

-- Function to return binary tree postorder traversal as a list
postorder :: Tree a -> [a]
postorder Null = []
postorder (Node x left right) = postorder left ++ postorder right ++ [x]
