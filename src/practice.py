class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            # the new value must go on the left
            if self.left in None:
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
    
    def search(self, target):
                


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
