#coding:utf8


class Solution(object):
    def search_word_util(self, board, row, col, word):
        if len(word) == 0:
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0]:
            return False

        board[row][col] = " "
        print board
        if self.search_word_util(board, row-1, col, word[1:]):
            return True
        if self.search_word_util(board, row+1, col, word[1:]):
            return True
        if self.search_word_util(board, row, col-1, word[1:]):
            return True
        if self.search_word_util(board, row, col+1, word[1:]):
            return True

        board[row][col] = word[0]
        print board
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m,n = len(board),len(board[0])


        def find(result,x,y,word,check):
            # if x==0 and y==3:
            #     print 'this is',result

            # print result
            if result==word:
                return True
            if 0<=x<=m-1 and 0<=y<=n-1 and board[x][y]==word[len(result)] \
                and (x,y) not in check:
                check.append((x,y))
                result+=board[x][y]
                print result,check,'//',(x,y)
                f = [(1,0),(-1,0),(0,-1),(0,+1)]
                for i,s in f:
                    print x+i,y+s
                    find(result,x+i,y+s,word,check)  #问题出在check上
            # else:
            #     return 'exit'
        for i in range(m):
            for y in range(n):
                # try: find('',i,y,word,[])
                # except:return True
                #f = find('',i,y,word,[])
                f = self.search_word_util(board,i,y,word)
                return f
        return False

s = Solution()
# print s.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ],"ABCCED")
#
# print s.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ],"ABG")

print s.exist(
        [["A","B","C","E"],
         ["B","F","E","S"],
         ["A","D","E","E"]
         ],"ABCESEEEF")
'''
A [(0, 0)] // (0, 0)
1 0
AB [(0, 0), (1, 0)] // (1, 0)
2 0
0 0
1 -1
1 1
-1 0
0 -1
0 1
AB [(0, 0), (1, 0), (0, 1)] // (0, 1)
1 1
-1 1
0 0
0 2
ABC [(0, 0), (1, 0), (0, 1), (0, 2)] // (0, 2)
1 2
ABCE [(0, 0), (1, 0), (0, 1), (0, 2), (1, 2)] // (1, 2)
2 2
0 2
1 1
1 3
ABCES [(0, 0), (1, 0), (0, 1), (0, 2), (1, 2), (1, 3)] // (1, 3)
2 3
ABCESE [(0, 0), (1, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)] // (2, 3)
3 3
1 3
2 2
ABCESEE [(0, 0), (1, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 2)] // (2, 2)
3 2
1 2
2 1
2 3
2 4
0 3
ABCESE [(0, 0), (1, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 2), (0, 3)] // (0, 3)
1 3
-1 3
0 2
0 4
1 2
1 4
-1 2
0 1
0 3
None
'''