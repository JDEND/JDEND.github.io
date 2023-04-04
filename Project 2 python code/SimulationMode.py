import random
import json
from datetime import datetime


class simulationMode:
    def simulationMode():
        time= datetime.now()
        time = time.strftime("%H:%M:%S, %m/%d/%Y")
        revenue=0
        cost=0
        employee=['Ali','Huy','Ian','Alex','Jared']
        with open('AppData.json','r') as openfile:
                Data=json.load(openfile)
        regPrice= 0.77; espressoPrice=0.78; lattePrice=0.866; capaPrice=0.7788; cocoaPrice=1.2043
        for i in range(100):
            reg=random.randrange(3); espresso=random.randrange(3); latte=random.randrange(3)
            capa=random.randrange(3);cocoa=random.randrange(3)
            costOforder=(reg*regPrice)+(espresso*espressoPrice)+(latte*lattePrice)+(capa*capaPrice)+(cocoa*cocoaPrice)
            total=(reg*Data['prices']['regular'])+(espresso*Data['prices']['expresso'])+(latte*Data['prices']['latte'])\
                +(capa*Data['prices']['cappa'])+(cocoa*Data['prices']['cocoaLatte'])
            if total==0:
                total=Data['prices']['regular']
                costOforder=0.77
                reg=1
            cost+=costOforder
            revenue+=total
            total="{:.2f}".format(total)
            log="simulation Mode#:"+str(Data['orderID'])+", Employee: "+str(random.choice(employee))\
                +", Order: regular "+str(reg)+", espresso "+str(espresso)+", latte "+str(latte)+", cappuccino "+str(capa)+", cocoa latte "\
                    +str(cocoa)+", total= "+str(total)+"$"+" at "+str(time)
            Data['logs'][Data['orderID']]=log
            Data['orderID']+=1
        revenue="{:.2f}".format(revenue)
        cost="{:.2f}".format(cost)
        gross="{:.2f}".format(float(revenue)-float(cost))
        margin="{:.2f}".format((float(gross)/float(revenue))*100)
        
        with open("AppData.json","w") as out:
           json.dump(Data,out)
        
        return "Results:\nRevenue: "+str(revenue)+"$\n"+"cost: "+str(cost)+"$\n"+"Gross Profit: "\
            +str(gross)+"$\n"+"Gross Margin: "+str(margin)+"%"
         
        
        


