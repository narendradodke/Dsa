from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        queue = deque([beginWord])
        visited = {beginWord}
        found = False

        while queue and not found:
            levelVisited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        newWord = word[:i] + c + word[i + 1:]

                        if newWord in wordSet and newWord not in visited:
                            if newWord not in levelVisited:
                                levelVisited.add(newWord)
                                queue.append(newWord)

                            parents[newWord].append(word)

                            if newWord == endWord:
                                found = True

            visited.update(levelVisited)

        if not found:
            return []

        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)
        return result