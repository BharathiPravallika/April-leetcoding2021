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
