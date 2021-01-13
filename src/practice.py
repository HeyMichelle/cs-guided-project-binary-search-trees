class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            # the new value must go on the left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
                # you can have child node figure it out via recursion
                # when I'm at node 8 I don't know where to go, 5 on left or right? what about 7? 
                # right and left of the node are already tree in themselves, and we know that they have to have an insert, we can pass the value onto that child and have it figure it out. If they can't, they will pass it to the next child. 
                
        else:
            # the value must go right
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)
    
    # this will always return true or false if the item is not at the current node, what is if we need to search further? see next code, lol
    def search(self, target):
        # the first thing to check when finding a value in the tree
        # check against the root, check to see if target item even exists
        if target == self.value:
            # we have found the item
            return True
        if target < self.value:
            # search the left side of the tree
            # if we found nothing, then we know it's pointing to none
            if self.left is None:
                return False
            return self.left.search(target) 
            # if a node exists to the left, call search on that node. This allows us to search the next node
                
        else:
            # Search the right side of the tree
            if self.right is None:
                return False
            return self.right.search(target) # check to see if item is at the next node, it will return true 
            # true is the value it will carry back and traverse back to the root with the returned-value. 
            # Now we're back to the initial function call that started this whole thing with self is = 9 
            # we push up calls and wait for them to give us the answer, true or false, passing it on to each function 
        
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()

        print(self.value)

        if self.right is not None:
            self.right.print_tree()


root = BSTNode(8)
root.insert(5)
root.insert(7)
root.insert(12)
root.insert(11)

print(root.search(7))
print(root.search(9))

root.insert(9)
print(root.search(9))
print(root.print_tree()) # to print whole tree

# what is the runtime of print? 
    # how many nodes do you have to visit?
    # linear O(n), you'll finish every single node

# this differs from the SEARCH function O(log(n)) WOOT WOOT! because once found you can skip entire parts of your data structure (hopefully by half - if A balanced tree).

# Binary Search Trees
    # all values on left must be smaller than the parent node
    # all values on the right must be greater
    # e.g.: note* this is a relatively balanced tree, and can be viewed as sub trees (recursive definitions) and start of trees
        #              root
        #               8
        #       6               10
        #   none    8       9       11
        #                               12 (if we added 12 this is where it would have to go) 
        #                                  (looks similar to how linked lists are and could end up with O(n) time if, for ex, 1-2-3-4-5 searching for 5)
        # 
        # what if we are deciding where to insert something? Let's say an 8?
        # items that are <= go on the left
        # 
        # 
        # insert is great because you don't have to shift
        # what if there were hundres of items on the left? no need to shift through them with insert or searching through the whole space
        # 
        # ### if given 5, where would you put it? On the left, because <= 8
        #              root
        #               8
        #   (5 wud go hur)      none    
        # none      none
        # 
        # if there is no node on the left
        # we create a new node
        # else the value goes to the right
        # for purpose of notes, the number 8 is considered self in the example above
        # every node points to none in both directions
