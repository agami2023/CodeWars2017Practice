class ponyMon:
    
    def __init__(self, name, ptype, weakness, resistance, HP, A1name, powreq1, dam1, A2name, powreq2, dam2):
        self.name = name
        self.ponyType = ptype
        self.weakness = weakness
        self.resistance = resistance
        self.HP = int(HP)
        self.attackName1 = A1name
        self.powreq1 = int(powreq1)
        self.damage1 = int(dam1)
        self.attackName2 = A2name
        self.powreq2 = int(powreq2)
        self.damage2 = int(dam2)
    
    def fightSim(pony1, pony2):
        print("Matchup: ", pony1.name, " fights ", pony2.name)
        # set 0 charge
        p1PowCharge = 0
        p2PowCharge = 0
        # get health of each pony
        p1Health = pony1.HP
        p2Health = pony2.HP
        # get attack values and the power requirement of both ponymon 
        if pony1.powreq1 < pony1.powreq2:
            p1Attack = pony1.damage1
            p1req = pony1.powreq1
        elif pony1.powreq1 == pony1.powreq2:
            if pony1.damage1 > pony1.damage2:
                p1Attack = pony1.damage1
                p1req = pony1.powreq1
            else: 
                p1Attack = pony1.damage2
                p1req = pony1.powreq1
        else:
            p1Attack = pony1.damage2
            p1req = pony1.powreq2
        if pony2.powreq1 < pony2.powreq2:
            p2Attack = pony2.damage1
            p2req = pony2.powreq1
        elif pony2.powreq1 == pony2.powreq2:
            if pony2.damage1 > pony2.damage2:
                p2Attack = pony2.damage1
                p2req = pony2.powreq1
            else: 
                p2Attack = pony2.damage2
                p2req = pony2.powreq1        
        else:
            p2Attack = pony2.damage2    
            p2req = pony2.powreq2
        # alter attack with respect to weakness/resistance
        if pony1.ponyType == pony2.weakness:
            p1Attack *= 2
        if pony1.ponyType == pony2.resistance:
            p1Attack /= 2
        if pony2.ponyType == pony1.weakness:
            p2Attack *= 2
        if pony2.ponyType == pony1.resistance:
            p2Attack /= 2
        
        # loop attacks until one pony has no health
        while p1Health > 0 and p2Health > 0:
            if p1PowCharge == p1req:
                p2Health -= p1Attack
                p1PowCharge -= p1req
            if p2PowCharge == p2req and p2Health > 0:
                p1Health -= p2Attack
                p2PowCharge -= p2req
            p1PowCharge += 1
            p2PowCharge += 1    
        if p1Health > p2Health:
            print(pony1.name, " defeats ", pony2.name, " with ", p1Health, " HP remaining.")
        else: print(pony2.name, " defeats ", pony1.name, " with ", p2Health, " HP remaining.")
            
# get input
ponies = int(input())
ponyList = []
while ponies > 0:
    ponyList.append(ponyMon(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    ponies -= 1
i = 0
while i < len(ponyList):
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 = input().split()
    ponyList[i] = ponyMon(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)
    i+=1
# get fight matchups
fights = int(input())
fightList = []
while fights > 0:
    f1, f2 = input().split()
    fightList.append(f1)
    fightList.append(f2)
    fights-=1

fightListPonies = []
for i in fightList:
    for j in ponyList:
        if j.name == i:
            fightListPonies.append(j)

while len(fightListPonies) >= 1:
    fightListPonies[0].fightSim(fightListPonies[1])
    fightListPonies.pop(0)
    fightListPonies.pop(0)