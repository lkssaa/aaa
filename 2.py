f = open("cipher7.txt","r", encoding="utf-8")
s=''
for line in f:
    for i1 in range(0,len(line)-6, 6):
            s+=str(line)[i1+4]
            s+=str(line)[i1]
            s+=str(line)[i1+3]
            s+=str(line)[i1+2]
            s+=str(line)[i1+5]
            s+=str(line)[i1+1]
f.close()
my_file = open("rascipher7.txt", "w", encoding="utf-8")
my_file.write(s)
my_file.close()