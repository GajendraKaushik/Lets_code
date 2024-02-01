class Solution:
    def exist(self, board, word) -> bool:
        from collections import Counter
        
        R = len(board)
        C = len(board[0])
        # if lenth of word is greater then the tolal letters in board then return false
        if len(word) > R*C:
            return False
        
        # creating a hash table of board with frequency of each word 
        count = Counter(sum(board, []))

        # compairing the frequency of each letter in word and board if frequency of letters is less in board then word we will return false 
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
        # if frequency of starting letter is more than the end letter then we will reverse the word it will hehlp in back tracking    
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]

        # using set to store the uniqe letter position              
        ans = set()
        
        def recursive(r, c, i):
            # Base case
            if i == len(word):
                return True
            # edge cases 
            if r < 0 or c < 0 or r >= R or c >= C or word[i] != board[r][c] or (r,c) in ans:
                return False
            # add letter index in ans
            ans.add((r,c))

            # checking all the adjacent of a letter for the next 
            res = (
                recursive(r+1,c,i+1) or 
                recursive(r-1,c,i+1) or
                recursive(r,c+1,i+1) or
                recursive(r,c-1,i+1) 
            )

            ans.remove((r,c))  #backtracking

            return res
        
        # colling the 
        for i in range(R):
            for j in range(C):
                if recursive(i,j,0):
                    return True
        
        return False