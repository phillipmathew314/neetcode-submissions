class TrieNode:
    def __init__(self):
        self.data = {}
        self.isWord = False
    
    def addWord(self, word):
        cur_node = self
        for char in word:
            if char not in cur_node.data:
                cur_node.data[char] = TrieNode()
            cur_node = cur_node.data[char]
        cur_node.isWord = True
    
    def removeWord(self, word) -> bool:
        def dfs(ind, cur_node):
            char = word[ind]
            print(char)
            if ind < len(word) - 1:
                isEmpty = dfs(ind+1, cur_node.data[char])
                if isEmpty:
                    cur_node.data.pop(char)
            
            if ind == len(word) - 1:
                cur_node.data[char].isWord = False
            
            return len(cur_node.data.keys()) == 0 and not cur_node.isWord
        
        dfs(0, self)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first form a trie from the words list
        # then go through board doing a dfs at each cell. during dfs keep track of visited map
        # at each char, check isWord. if true, add to the result set.
        # if you find a word from the trie, then you can remove it from the trie so you don't have to re-check it
        # finally, convert the result set to a list
        trie = TrieNode()
        for word in words:
            trie.addWord(word)
        
        res = []
        def dfs(row, col, seen, trieNode, cur_word):
            nonlocal res
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            for dx, dy in dirs:
                if 0 <= row+dx < len(board) and 0 <= col+dy < len(board[0]) and not seen[row+dx][col+dy] and board[row+dx][col+dy] in trieNode.data:
                    char = board[row+dx][col+dy]
                    seen[row+dx][col+dy] = True
                    dfs(row+dx, col+dy, seen, trieNode.data[char], cur_word + char)
                    seen[row+dx][col+dy] = False
                
            if trieNode.isWord:
                res.append(cur_word)
                trieNode.isWord = False
                # if not trieNode.data:
                # trie.removeWord(cur_word)

        seen = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                seen[r][c] = True
                char = board[r][c]
                if char in trie.data:
                    dfs(r, c, seen, trie.data[char], char)
                seen[r][c] = False
        
        return res