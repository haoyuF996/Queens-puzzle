import random,math,copy
n,WinList,trys = int(input('n:')),[],0
QueenList = list(range(n))
while trys<=math.factorial(n)*2 :
    random.shuffle(QueenList)
    trys+=1
    Goo = True
    for i,v in enumerate(QueenList):
        for k,l in enumerate(QueenList):
            if i!=k and abs((v-l)/(k-i)) == 1:
                Goo = False
    if Goo:
        if not QueenList in WinList:
            WinList.append(copy.deepcopy(QueenList))
            print(f'Found {QueenList} in {trys} trys(NO.{len(WinList)})')
            trys = 0
print(f'There are {len(WinList)} solutions')