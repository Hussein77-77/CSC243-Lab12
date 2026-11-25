count=0
records=[]
try:
   with open("scores.txt","r") as f:
    for line in f:
        fields=line.rstrip().split(",")
        if not fields[1].isdigit():
            continue
        else:
         count+=1
         name=fields[0]
         score=int(fields[1])
         if name=="Karim":
            karim_score=score
    with open("scores.txt") as f:
        for line in f:
            fields=line.rstrip().split(",")
            if not fields[1].isdigit():
                continue
            else:
             name=fields[0]
             score=int(fields[1])
             if name=="Nour":
               continue
             if name=="Maya":
               score=88
             records.append([name,score])
except FileNotFoundError:
    print("File not found.")
else:
    print(karim_score)
    print(count)
    with open("scores.txt","w") as f:
       for name,score in records:
        f.write(f"{name},{score}\n")
    with open("pass.txt","w") as f:
        for name,score in records:
            if score>=60:
                f.write(name+"\n")

        