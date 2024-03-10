import heapq

class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None  

def getcode(tree):
    slovar = {}
    for i, i1 in tree:
        slovar[i] = i1
    return slovar

def isb(slovar, text):
    length = 0
    for i in text:
        length += len(slovar[i])
    r = length / len(text)
    return r

def btree(slovar):
    heap = [[weight, [char, ""]] for char, weight in slovar.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for i in lo[1:]:
            i[1] = '0' + i[1]
        for i in hi[1:]:
            i[1] = '1' + i[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

f = open("text07.txt", encoding='utf-8')
a=f.readline()
f.close()
b={}
c=0
for i in "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ ":
    exec("b['%s']=0;" % i)
for i in a:
    b[i]+=1
b = dict(sorted(b.items(), key=lambda x: x[1]))
b.pop('Ъ')
b.pop('Ф')
t=btree(b)
ans=getcode(t)
f=open("a1.txt", 'w')
re = isb(ans, a)
print(ans)
print(re)
for i in a:
    f.write(ans[i])