class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        wordList.append(beginWord)
        
        wordMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)): # Add "cat" to "*at", "c*t", and "ca*"
                pattern = word[:i] + "*" + word[i + 1:]
                wordMap[pattern].append(word)
        
        queue = deque([beginWord])
        visited = set([beginWord])
        res = 1

        while queue:
            for i in range(len(queue)):
                curWord = queue.popleft()
                if curWord == endWord:
                    return res
                for j in range(len(curWord)):
                    pattern = curWord[:j] + "*" + curWord[j + 1:]
                    for neighborWord in wordMap[pattern]:
                        if neighborWord not in visited:
                            queue.append(neighborWord)
                            visited.add(neighborWord)
            res += 1
        
        return 0
