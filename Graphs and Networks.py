
# coding: utf-8

# In[1]:



def graph_creation(dicts):
    graph={}
    for i in dicts.keys():
        graph[i]=dicts.get(i)
    return graph
def add_links(graph , dicts):
    for i in dicts.keys():
        for g in graph.keys():
            if g in dicts[i] and i not in graph[g]:
                graph[g]=graph[g]+[i]
        graph[i]=dicts[i]

def fix_graph(graph):
    for g in graph.keys():
        for v in graph[g]:
            if not g in graph[v]:
                graph[v] = graph[v]+ [g]
         

        
        

def connected_graph(graph):
    for node in graph.keys():
        if eulerianfirst(graph,node) :
            print('All Nodes Are Connected')
            return
    print('Some of the Nodes Arent Connected')
    
    
def eulerianfirst(graph,key):
    if key not in graph.keys():
        print('Key Dont Exist')
        return
    b=False
    b2=False
    check2=graph.keys()
    check=[key]
    for i in graph[key]:
        if b:
            break
        if i not in check:
            b=eulerian(graph,i,b,check,check2,b2)
            if b:
                if check[0] in graph[check[-1]]: print(f'{check} is a  Eulerian Cycle')
                else:print(f'{check} is  Eulerian path')
                return True
            else:
                check=[key]
    print(f'There arent any Eulerian paths that begin in {key.upper()}')
    return False    
        
def eulerian(graph,key,b,check,check2,b2):
    check.append(key)
    print(check)
    if (len(check)==len(check2) and set(check)==set(check2)) or b==True:
        b=True
        return True
    elif len(set(check)) != len(check) :
        return False
    
    for i in graph[key]:
        if i not in check:
            temp=check
            b=eulerian(graph,i,b,temp,check2,b2)
            if b:
                return True  
            else:temp.pop()
                
                
def Dijkstrafirst(graph,start,end):
    bank=[]
    if  start==end :
        print('both keys are the same not road need to be taken')
    for i in graph[start]:
        check=[start]
        if i not in check:
            dijkstra(graph,i,end,check,bank)
    shortest=bank[0]
    for i in bank:
        if len(i) < len(shortest) :
            shortest=i
    d=[]
    for i in bank:
        if len(i) ==len(shortest) and i != shortest:
            d.append(i)
    if len(d)>0:
        print(f'the shortest routes have {len(shortest)} and the routes are :')
        print(shortest)
        for i in d:
            print(i)
    else:        
        print('')
        print(f'the shortest route is {shortest} of {len(shortest)} steps')
            
def dijkstra(graph,start,end,check,bank):                
    check.append(start)
    if  start==end:
        bank.append(tuple(check))
    if set(check)==set(graph.keys()):
        return
    
    for i in graph[start]:
        temp=check
        if i not in check:
            dijkstra(graph,i,end,temp,bank)
            temp.pop()
    
                
                
                
                
                
                
                
                
                
                
                
graph=  { "a" : ["c",'b'],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c",'a'],
          "e" : ["c", "b"],
        }
graph2=  { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b"],
          "d" : ["e"],
          "e" : ["d", "b"],
        }                
Dijkstrafirst(graph,'a','e')        
    
 

