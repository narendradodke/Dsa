class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        if len(word) > m * n:
            return False

        from collections import Counter

        board_count = Counter(char for row in board for char in row)
        word_count = Counter(word)

        for char, count in word_count.items():
            if board_count[char] < count:
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(r, c, index):
            if index == len(word):
                return True

            if (r < 0 or r >= m or c < 0 or c >= n
                    or board[r][c] != word[index]):
                return False

            char = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )

            board[r][c] = char
            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False