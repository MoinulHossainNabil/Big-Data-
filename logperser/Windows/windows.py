import json
path="/home/bjit-542/Big Data/logperser/Windows/Windows_2k.log"
logfile=open(path)
dataset=[]
for line in logfile:
    l=line.split(" ")
    dataset.append(l)
    #print(l)
result=[]
for d in dataset:
    if(d[2]=="Info"):
        message=d[24:]
        output={
            "timestamp":d[0]+d[1],
            "level":d[2],
            "logs":d[20],
            "message":message
        }
        result.append(output)
for r in result:
    print(r)
jsonfilepath="/home/bjit-542/Big Data/logperser/Windows/Windows.json"
with open(jsonfilepath,'w') as outputfile:
    json.dump(result,outputfile)



