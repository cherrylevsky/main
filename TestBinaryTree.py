

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

  def __str__(self):
    return str(self.data)

class Tree (object):
  def __init__ (self):
    self.root = None

  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
            current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode
    

  # Returns true if two binary trees are similar
  def isSimilar (self, pNode):
    if type(pNode) != Tree:#not similar if diff. types
        return False
    else:
        selfCurrent = self.root
        otherCurrent = pNode.root #will traverse the two lists same node at a time
        return self.isSimilarHelper(selfCurrent, otherCurrent)

  def isSimilarHelper(self, selfCurrent, otherCurrent):
    if selfCurrent == None or otherCurrent == None:
        if selfCurrent == None and otherCurrent == None:
            return True #nodes are still equal since they are both None
        else:
            return False #one of the Nodes in that place has a value while the other is None
    else:
        if self.isSimilarHelper(selfCurrent.lChild, otherCurrent.lChild): #traversed the left side and found no mismatches
            if self.isSimilarHelper(selfCurrent.rChild, otherCurrent.rChild): #now try the right side
                return True #no mismatches found on right side
            else:
                return False #mismatch found, return False
        else:
            return False #mismatch on left side found, return False

  # Prints out all nodes at the given level
  def printLevel (self, level):
    if level <= 0:
        print "No nodes at that level"
    else:
        current = self.root
        print self.printLevelHelper(level, current, "")

  #helper for printLevel
  #creates and returns a string with all the elements on that particular level
  def printLevelHelper(self, level, current, string):
    level -= 1 #go down 1 level every time you traverse
    
    if level == 0: #base case; on the correct level; print the node
        if current != None:
            string += str(current) + "  "
            return string
        else:
            return string
    else:
        if current == None:#if the level has not been reached but the current node is None, return the current string
            return string
        else:
            string = self.printLevelHelper(level, current.lChild, string) #traverse and get left nodes at next level
            string = self.printLevelHelper(level, current.rChild, string) #traverse and get right nodes at next level
            return string

  # Returns the height of the tree
  def getHeight (self):
    current = self.root
    if current == None:
        return 0
    else:
        height = self.getHeightHelper(current, 0) - 1 #height == number of levels minus 1
        return height

  #helper for getHeight
  #returns number of levels in the binary tree
  def getHeightHelper(self, current, maxHeight):
    if current == None:
        return maxHeight #don't add anything to max, just return it
    else:
        #maxHeight += 1
        leftSide = self.getHeightHelper(current.lChild, maxHeight+1) #traverse left side for max
        rightSide = self.getHeightHelper(current.rChild, maxHeight+1) #traverse right side for max

        return max(leftSide,rightSide) #compare right and left sides for max

  def isBST(self):
    current = self.root
    if self.root != None:
      return self.isBinary(current)
    else:
      return False

  def isBinary(self, current):
    if current.lChild == None and current.rChild == None:
      return True
    elif current.lChild == None or current.rChild == None:
      if current.lChild == None:
        return current.rChild.data > current.data
      else:
        return current.lChild.data < current.data
    elif current.lChild.data > current.rChild.data:
      return False
    else:
      leftSide = self.isBinary(current.lChild)
      rightSide = self.isBinary(current.rChild)
      if leftSide == False or rightSide == False:
        return False
      else:
        return True

  def isFull(self):
    current = self.root
    if self.root != None:
      return self.isFullHelper(current)
    else:
      return False


  def isFullHelper(self, current):
    if current.lChild == None and current.rChild == None:
      return True
    elif current.lChild == None or current.rChild == None:
      return False
    else:
      leftSide = self.isFullHelper(current.lChild)
      rightSide = self.isFullHelper(current.rChild)
      if leftSide == False or rightSide == False:
        return False
      else:
        return True
      
      
    
    
    
def main():
    # Create three trees - two are the same and the third is different
    #tree 1
    t1 = Tree()
    t1.insert(8)
    t1.insert(4)
    t1.insert(5)
    t1.insert(1)
    t1.insert(2)
    t1.insert(15)
    t1.insert(13)
    t1.insert(20)
    t1.insert(17)
    t1.insert(21)

    print t1.isBST()

    t = Tree()
    t.insert(10)
    t.insert(5)
    t.insert(3)
    t.insert(7)
    t.insert(13)
    t.insert(12)
    t.insert(14)

    print t.isFull(), "is full"

    #tree 2 (equal to tree 1)
    t2 = Tree()
    t2.insert(8)
    t2.insert(4)
    t2.insert(5)
    t2.insert(1)
    t2.insert(2)
    t2.insert(15)
    t2.insert(13)
    t2.insert(20)
    t2.insert(17)
    t2.insert(21)

    print t2.isBST()
    
    #tree 3
    t3 = Tree()
    t3.insert(8)
    t3.insert(4)
    t3.insert(5)
    t3.insert(1)
    t3.insert(2)
    t3.insert(13)
    t3.insert(20)
    t3.insert(17)
    t3.insert(21)
    t3.insert(22)

    print t3.isBST()

    # Test your method isSimilar()
    print "Test to see that two trees are similar"
    print "Tree 1 is similar to Tree 2 (they are equal): ", t1.isSimilar(t2)
    print "Tree 1 is similar to Tree 3: ", t1.isSimilar(t3)
    print "**************************************************"
    print
    
    # Print the various levels of two of the trees that are different
    print "Test for printing levels a tree"
    t4 = Tree()
    print "Empty Tree at level 1: "
    t4.printLevel(1)
    print "Empty Tree at level 2: "
    t4.printLevel(2)
    print "Tree 1:"
    print "at level 1:"
    t1.printLevel(1)
    print "at level 2:"
    t1.printLevel(2)
    print "at level 3:"
    t1.printLevel(3)
    print "at level 4:"
    t1.printLevel(4)
    print "at level 5 (Tree 1 doesn't have level 5):"
    t1.printLevel(5)
    
    print "Tree 3:"
    print "at level 1:"
    t3.printLevel(1)
    print "at level 2:"
    t3.printLevel(2)
    print "at level 3:"
    t3.printLevel(3)
    print "at level 4:"
    t3.printLevel(4)
    print "at level 5:"
    t3.printLevel(5)
    print "at level 5 (Tree 3 doesn't have level 6):"
    t3.printLevel(6)
    print "**************************************************"
    print

    # Get the height of the two trees that are different
    print "Test for getting the height of a tree"
    print "Height of an empty tree: "
    print t4.getHeight()
    print "Height of Tree 1:"
    print t1.getHeight()
    print "Height of Tree 2 (equal to Tree 1):"
    print t2.getHeight()
    print "Height of Tree 3:"
    print t3.getHeight()
    

main() 
