class PrefixTree:
    class PrefixTreeNode:
        def __init__(self, isWord=False):
            self.data = {}
            self.isWord = isWord

    def __init__(self):
        # need map of letter to tuple.
        self.data = self.PrefixTreeNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        cur_node = self.data
        for char in word:
            if char not in cur_node.data:
                cur_node.data[char] = self.PrefixTreeNode(False)
            cur_node = cur_node.data[char]
        cur_node.isWord = True

    def search(self, word: str) -> bool:
        cur_node = self.data
        for char in word:
            if char in cur_node.data:
                cur_node = cur_node.data[char]
            else:
                return False
        return cur_node.isWord

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.data
        for char in prefix:
            if char in cur_node.data:
                cur_node = cur_node.data[char]
            else:
                return False
        return True
        