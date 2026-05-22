class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        wordList.append(beginWord)
        
        wordNeighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                wordNeighbors[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for wordNeighbor in wordNeighbors[pattern]:
                        if wordNeighbor not in visited:
                            visited.add(wordNeighbor)
                            queue.append(wordNeighbor)
            res += 1
        return 0
