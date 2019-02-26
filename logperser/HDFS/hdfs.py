import json
path="/home/bjit-542/Big Data/logperser/HDFS/HDFS_2k.log"
logfile=open(path)
dataset=[]
for line in logfile:
    l=line.split(" ")
    dataset.append(l)
    #print(l)
result=[]

for d in dataset:
    #print(d)
    #if(True):
    message = ""
    for d1 in range(5, len(d), 1):
        message = message + " " + d[d1]
    output = {
        "timestamp": d[0] + d[1] + d[2],
        "level": d[3],
        "component": d[4],
        "event_template": message
        # "parameters":d[7]+d[10]+d[12]

    }
    result.append(output)
for r in result:
    print(r)
jsonfilepath="/home/bjit-542/Big Data/logperser/HDFS/HDFS.json"
with open(jsonfilepath,'w') as outputfile:
    json.dump(result,outputfile)

#for k in
#7  10 12



