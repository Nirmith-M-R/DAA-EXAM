#10 Brute Force O(n!)
def backtrack(r,n):
    if r == n:
        res.append([" ".join(row) for row in board])
        return
    
    for c in range(n):
        if c in col or r+c in posdiag or r-c in negdiag:
            continue
    
        col.add(c)
        posdiag.add(r+c)
        negdiag.add(r-c)
        board[r][c] = 'Q'

        backtrack(r+1,n)

        col.remove(c)
        posdiag.remove(r+c)
        negdiag.remove(r-c)
        board[r][c] = '_'

n = int(input("Enter board size: "))
board = [["_"]*n for i in range(n)]
col = set()
posdiag = set()
negdiag = set()
res = []

backtrack(0,n)

print(res)