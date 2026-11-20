class WordDictionary:
    # just keep the same trie structure, but now add a . and isWord == True if ANY letter for the data == True
    class TrieNode:
        def __init__(self, isWord=False):
            self.data = {}
            self.isWord = isWord
    
    def __init__(self):
        self.data = self.TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.data
        for char in word:
            if char not in cur_node.data:
                cur_node.data[char] = self.TrieNode()
            cur_node = cur_node.data[char]
        
        cur_node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(ind, node) -> bool:
            cur_node = node
            i = 0
            while ind < len(word):
                char = word[ind]
                if char in cur_node.data:
                    cur_node = cur_node.data[char]
                    ind += 1
                elif char == ".":
                    if not cur_node.data:
                        return False
                    for c in cur_node.data.values():
                        val = dfs(ind+1, c)
                        if val: 
                            return True
                    return False
                else:
                    return False
            return cur_node.isWord

        return dfs(0, self.data)

