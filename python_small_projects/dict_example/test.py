"""
result[course][max/min/avg]
result["english"]["max"]=95
result["english"]["min"]=65
result["english"]["avg"]=45

"""
result={}

with open("score.txt") as fin:
    for line in fin:
        if len(line.strip())>0:
            line=line.strip()
            fields=line.split("\t")
            name,course,score=fields
            if course not in result:
                result[course]={}
                result[course]["avg"]=0
                result[course]["max"]=0
                result[course]["min"]=120
                result[course]["sum"]=0
                result[course]["count"]=0
            score=int(score)
            if score> result[course]["max"]:
                result[course]["max"]=score
            if score< result[course]["min"]:
                result[course]["min"]=score
            result[course]["count"] += 1
            result[course]["sum"] += score
            result[course]["avg"]=result[course]["sum"]/result[course]["count"]

for i in result.values():
    del i['count']
    del i['sum']

for k,v in result.items():
    output=[k,"max:"+str(v["max"]),'min:'+str(v['min']),"avg:"+str(v['avg'])]
    print(output)
