import json
path="/home/bjit-542/Big Data/logperser/Linux/Linux_2k.log"
logfile=open(path)
dataset=[]
for line in logfile:
    l=line.split(" ")
    dataset.append(l)
    #print(l)
result=[]
for d in dataset:
    if(d[5]=="authentication"):
        user=d[7:]
        output={
            "month":d[0],
            "day":d[1],
            "time":d[2],
            "type":d[3],
            "protocol":d[4],
            "mesaage":d[5]+d[6],
            "userprofile":user
        }
        result.append(output)
for r in result:
    print(r)
jsonfilelpath="/home/bjit-542/Big Data/logperser/Linux/Linux.json"
with open(jsonfilelpath,'w') as outputfile:
    json.dump(result,outputfile)




#for k in
#7  10 12



