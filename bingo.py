import colorama
from colorama import Fore,Style
import random
mat=[[None for j in range(5)]for i in range(5)]
#generating random matrix
avail=set([(i,j) for j in range(5) for i in range(5)])
c=1
while(len(avail)):
	selected=random.choice(list(avail))
	avail=avail-{selected}
	mat[selected[0]][selected[1]]=c
	c+=1
#displaying generated matrix
for i in range(5):
	for j in range(5):
		print("%02d"%mat[i][j],end=" ")
	print()
print()
#initializing required data for game
crossed=[[False for i in range(5)] for j in range(5)]
priority={i:0 for i in range(1,26)}
conected={i:0 for i in range(1,26)}
striked=set()
#game loop
while(len(striked)<25):
	l=list(map(int,input("Enter numbers to strike : ").split()))
	#strike the numbers
	for i in range(5):
		for j in range(5):
			if(mat[i][j] in l ):
				crossed[i][j]=True
	striked|=set(l)
	#display matrix
	for i in range(5):
		for j in range(5):
			if(crossed[i][j]==False):
				print("%02d"%mat[i][j],end=" ")
			else:
				print((Fore.RED+"%02d"+Style.RESET_ALL)%mat[i][j],end=" ")
		print()
	#calc prority and check for bingo
	bingo=0
	for i in range(5):
		v=crossed[i].count(True)
		if(v==5):
			bingo+=1
		elif(v==0):
			continue
		for j in range(5):
			if(crossed[i][j]==False):
				priority[mat[i][j]]=max(priority[mat[i][j]],v)
				conected[mat[i][j]]=conected[mat[i][j]]+1
	zippedcross=list(zip(*crossed))
	for i in range(5):
		v=zippedcross[i].count(True)
		if(v==5):
			bingo+=1
		elif(v==0):
			continue
		for j in range(5):
			if(zippedcross[i][j]==False):
				priority[mat[j][i]]=max(priority[mat[j][i]],v)
				conected[mat[j][i]]=conected[mat[j][i]]+1
	maind=sum([1 for i in range(5) if crossed[i][i]])
	secd=sum([1 for i in range(5) if crossed[i][5-i-1]])
	if(maind==5):
		bingo+=1
	if(secd==5):
		bingo+=1
	if(maind!=0):
		for i in range(5):
			if(crossed[i][i]==False):
				priority[mat[i][i]]=max(priority[mat[i][i]],maind)
				conected[mat[i][i]]=conected[mat[i][i]]+1
	if(secd!=0):
		for i in range(5):
			if(crossed[i][5-i-1]==False):
				priority[mat[i][5-i-1]]=max(priority[mat[i][5-i-1]],secd)
				conected[mat[i][5-i-1]]=conected[mat[i][5-i-1]]+1
	#display recomended number
	if(bingo>=5):
		print(f"\n{Fore.YELLOW}BINGO{Style.RESET_ALL}")
		break
	ma=0
	recom=0
	for i,j in priority.items():
		if(j>ma or (recom!=0 and j==ma and conected[i]>conected[recom])):
			ma=j
			recom=i
	print("recomended number to strike next : ",end="")
	print(f"{Fore.GREEN}{recom}{Style.RESET_ALL}")
	print()
	#reseting priority for next iteration
	priority={i:0 for i in range(1,26)}
print("\nGood Game...! ")