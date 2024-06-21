import colorama
from colorama import Fore, Style
import random

n = int(input("Enter length of the board : "))
board = [[None for j in range(n)] for i in range(n)]

# generating random matrix
avail = set([(i, j) for j in range(n) for i in range(n)])
c = 1
while len(avail):
    selected = random.choice(list(avail))
    avail = avail - {selected}
    board[selected[0]][selected[1]] = c
    c += 1

# displaying generated matrix
for i in range(n):
    for j in range(n):
        print("%02d" % board[i][j], end=" ")
    print()
print()

# initializing required data for game
crossed = [[False for i in range(n)] for j in range(n)]
priority = {i: 0 for i in range(1, n * n + 1)}
conected = {i: 0 for i in range(1, n * n + 1)}
striked = set()

# game loop
while len(striked) < n * n:
    curr_stricked = list(map(int, input("Enter numbers to strike : ").split()))

    # strike the numbers
    for i in range(n):
        for j in range(n):
            if board[i][j] in curr_stricked:
                crossed[i][j] = True
    striked |= set(curr_stricked)

    # display matrix
    for i in range(n):
        for j in range(n):
            if crossed[i][j] == False:
                print("%02d" % board[i][j], end=" ")
            else:
                print((Fore.RED + "%02d" + Style.RESET_ALL) % board[i][j], end=" ")
        print()

    # calc prority and check for bingo
    bingo = 0
    for i in range(n):
        row_crossed_count = crossed[i].count(True)
        if row_crossed_count == n:
            bingo += 1
        elif row_crossed_count == 0:
            continue
        for j in range(n):
            if crossed[i][j] == False:
                priority[board[i][j]] = max(priority[board[i][j]], row_crossed_count)
                conected[board[i][j]] = conected[board[i][j]] + 1
    
    zippedcross = list(zip(*crossed))
    for i in range(n):
        row_crossed_count = zippedcross[i].count(True)
        if row_crossed_count == n:
            bingo += 1
        elif row_crossed_count == 0:
            continue
        for j in range(n):
            if zippedcross[i][j] == False:
                priority[board[j][i]] = max(priority[board[j][i]], row_crossed_count)
                conected[board[j][i]] = conected[board[j][i]] + 1
    
    maind = sum([1 for i in range(n) if crossed[i][i]])
    secd = sum([1 for i in range(n) if crossed[i][n - i - 1]])
    if maind == n:
        bingo += 1
    if secd == n:
        bingo += 1
    if maind != 0:
        for i in range(n):
            if crossed[i][i] == False:
                priority[board[i][i]] = max(priority[board[i][i]], maind)
                conected[board[i][i]] = conected[board[i][i]] + 1
    if secd != 0:
        for i in range(n):
            if crossed[i][n - i - 1] == False:
                priority[board[i][n - i - 1]] = max(priority[board[i][n - i - 1]], secd)
                conected[board[i][n - i - 1]] = conected[board[i][n - i - 1]] + 1
    
	# display recomended number
    if bingo >= n:
        print(f"\n{Fore.YELLOW}BINGO{Style.RESET_ALL}")
        break
    ma = 0
    recom = 0
    for i, j in priority.items():
        if j > ma or (recom != 0 and j == ma and conected[i] > conected[recom]):
            ma = j
            recom = i
    
    print("recomended number to strike next : ", end="")
    print(f"{Fore.GREEN}{recom}{Style.RESET_ALL}")
    print()
    
    # reseting priority for next iteration
    priority = {i: 0 for i in range(1, n*n+1)}
    conected = {i: 0 for i in range(1, n*n+1)}
print("\nGood Game...! ")
