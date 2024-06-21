import colorama
from colorama import Fore, Style
import random

n = int(input("Enter length of the board : "))
board = [[None for j in range(n)] for i in range(n)]

# generating random matrix
avail = set(range(1, n * n + 1))
element_to_index = {}
for i in range(n):
    for j in range(n):
        board[i][j] = random.choice(list(avail))
        element_to_index[board[i][j]] = (i, j)
        avail.remove(board[i][j])

# displaying generated matrix
for i in range(n):
    for j in range(n):
        print("%02d" % board[i][j], end=" ")
    print()
print()

# initializing required data for game
avail = set(range(1, n * n + 1))
striked_row = {i: 0 for i in range(n)}
striked_col = {i: 0 for i in range(n)}
striked_main_diag = 0
striked_sec_diag = 0


# game loop
while len(avail) > 0:

    # input for stricking numbers
    curr_stricked = list(map(int, input("Enter numbers to strike : ").split()))

    # strike the numbers
    for num in curr_stricked:
        if num not in avail:
            continue
        avail.remove(num)
        i, j = element_to_index[num]
        striked_row[i] += 1
        striked_col[j] += 1
        if i == j:
            striked_main_diag += 1
        if i == n - j - 1:
            striked_sec_diag += 1

    # display matrix
    for i in range(n):
        for j in range(n):
            if board[i][j] in avail:
                print("%02d" % board[i][j], end=" ")
            else:
                print((Fore.RED + "%02d" + Style.RESET_ALL) % board[i][j], end=" ")
        print()

    # check for bingo
    bingo = 0
    for i in range(n):
        bingo += striked_row[i] == n
        bingo += striked_col[i] == n
    bingo += striked_main_diag == n
    bingo += striked_sec_diag == n

    if bingo >= n:
        print(f"\n{Fore.YELLOW}BINGO{Style.RESET_ALL}")
        break
    
    # calculating priority for each number
    recomendation = -1
    max_priority = -1
    max_connections = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] in avail:
                priority = 0
                connections = 0
                priority = max(priority, striked_row[i])
                priority = max(priority, striked_col[j])
                if i == j:
                    priority = max(priority, striked_main_diag)
                    connections += 1
                if i == n - j - 1:
                    priority = max(priority, striked_sec_diag)
                    connections += 1
                if priority > max_priority or (priority == max_priority and connections > max_connections):
                    max_priority = priority
                    max_connections = connections
                    recomendation = board[i][j]
    
                
	# display recomended number
    print("recomended number to strike next : ", end="")
    print(f"{Fore.GREEN}{recomendation}{Style.RESET_ALL}")
    print()
    
   
print("\nGood Game...! ")
