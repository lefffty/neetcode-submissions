class PrefixNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def __contains__(self, char: str):
        return char in self.children


class WordDictionary:
    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node:
                node.children[char] = PrefixNode()
            node = node.children[char]

        node.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end_of_word
        return dfs(0, self.root)
