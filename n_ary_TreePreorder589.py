class Solution:
    def preorder(self, root: 'Node')->List[int]:
        return self._preorder(root, [])
    def _preorder(self, root:'Node', nodeList:[])->List[int]:
        if root is None:
            return nodeList
        nodeList.append(root.val)
        for child in root.children:
            self._preorder(child, nodeList)
        return nodeList
    
    
"""
#code to compile on general compilers
from collections import deque
# N-ary Tree యొక్క Node structure
class NewNode():
    def __init__ (self, val):
        self.key = val
        #లిస్ట్ లో అన్ని చిల్డ్రన్ నోడ్స్ స్టోర్ అవుతాయి - all children are stored in a list
        self.child = []
    #Utility function to print the preorder of the given N-ary Tree - (N-ary Tree యొక్క preorder ప్రింట్ చేయడానికి utility function)
    def preorderTraversal(root):
        stack = deque([])
        #'Preorder'->contains all the visited nodes(Preorder లో visited నోడ్స్ అన్ని ఉంటాయి  )
        preorder = []
        preorder.append(root.key)
        stack.append(root)
        while len(stack) > 0:
            #"Flag" checks whether all the child nodes have been visited(అన్ని నోడ్స్ ని విసిట్ చేసామో లేదో ఫ్లాగ్ చెక్ చేస్తుంది )
            flag=0
            #Case1-> If top of the stack is a leaf node then reomove it from the stack
            #Case1-> స్టాక్ లో టాప్ ఎలిమెంట్ లీఫ్ నోడ్ ఉంటే దాన్ని రిమూవ్ చేసేయండి 
            if len((stack[len(stack)-1]).child) == 0:
                x = stack.pop()
                #Case2-> If top of the stack is parent with children
            else:
                par = stack[len(stack)-1]
            #a)As soon as an unvisited child is found (left to right sequence), push it to stack and store it in auxillary list(Marked visited)
            #Start again from case-1, to explore this newly visited child.
            #అన్ విసితెద్ చైల్డ్ ని కనుగొన్న వెంటనే దాన్ని స్టాక్ లో పుష్ చేయండి తరువాత ఆక్సిలియరీ లిస్ట్ లో స్టోర్ చేయండి.
            #మల్లి కేస్1 దగ్గర నుండి స్టార్ట్ చేయండి  
        for i in range(0, len(par.child)):
            if par.child[i].key not in preorder:
                flag = 1
                stack.append(par.child[i])
                preorder.append(par.child[i].key)
                break;
                #If all child nodes from left to right of a parent have been visited then remove the parent from the stack
                #పేరెంట్ యొక్క అన్ని చైల్డ్ (left to right sequence)  విసిట్ చేసిన తర్వాత స్టాక్ నుండి ఆ పేరెంట్ ని రిమూవ్ చేయండి 
        if flag == 0:
            stack.pop()
    print(preorder)
if __name__ == '__main__' :
    root = NewNode(1)
    root.child.append(NewNode(2))
    root.child.append(NewNode(3))
    root.child.append(NewNode(4))
    root.child[0].child.append(NewNode(5))
    root.child[0].child[0].child.append(NewNode(10))
    root.child[0].child.append(NewNode(6))
    root.child[0].child[1].child.append(NewNode(11))
    root.child[0].child[1].child.append(NewNode(12))
    root.child[0].child[1].child.append(NewNode(13))
    root.child[2].child.append(NewNode(7))
    root.child[2].child.append(NewNode(8))
    root.child[2].child.append(NewNode(9))
    preorderTraversal(root)
"""
