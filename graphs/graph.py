
with open("connected.txt", "r") as c:
    connect = c.read().split("\n")
graph = []
keys = {}
for i in connect:
	if i == "":
		connect.remove(i)
		break
	k = i.split()[0]
	v = i.split()[1]
	keys = {*keys, k, v}
  
for o in range(len(keys)):
    graph.append([])


for i in connect:
	v = int(i.split()[1])
	k = int(i.split()[0])
	graph[k].append(v)
	graph[v].append(k)

			
def findPathSimple(s, b):
    visited = {s}
    stack= [s]
    path = []  
	
    while stack != []:
        top = stack[-1]
        path = [*path, top]
        neighboursOfTop  =  graph[top]
        if b in  neighboursOfTop:
            return path + [b]
        neighboursToCheck = [x for x in neighboursOfTop if x not in visited]
		
        if neighboursToCheck != []:
            nextTop = neighboursToCheck[-1]
            stack = [*stack, nextTop]
            visited = {*visited, nextTop}
        else:
            stack = stack[:-1]
            print("le", path[-1])
            path = path[:-2]     
    return  None

print(graph)
    
a = 2
b = 1

print(findPathSimple(a, b))



