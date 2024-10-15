# Just code to help you out here
import networkx as nx
import pandas as pd
import copy
from collections import Counter

def to_adj(T):
    try:
        return pd.DataFrame(nx.adjacency_matrix(T).todense(),index=T.nodes(),columns=T.nodes())
    except:
        print("Cannot convert to adjacency matrix")
    return None

def show(T):
    T = copy.deepcopy(T)
    width_dict = Counter(T.edges())
    edge_width = [ (u, v, {'width': value}) 
                  for ((u, v), value) in width_dict.items()]
    
    G_new = nx.DiGraph()
    G_new.add_edges_from(edge_width)
    pos=nx.kamada_kawai_layout(G_new)
    #pos=nx.spring_layout(G_new)
    nx.draw(G_new, pos)
    edge_labels=dict([((u,v,),d['width'])
                 for u,v,d in G_new.edges(data=True)])
    
    nx.draw(G_new,pos,with_labels=True)
    nx.draw_networkx_edges(G_new, pos=pos)
    nx.draw_networkx_edge_labels(G_new, pos, edge_labels=edge_labels,
                                 label_pos=0.55, font_size=10)
    
def composition(k,text):
    patterns = []
    # YOUR SOLUTION HERE
    ## BEGIN SOLUTION
    for i in range(0,len(text)-k+1):
        patterns.append(text[i:(i+k)])
    patterns.sort()
    ## END SOLUTION
    return patterns

def de_bruijn(patterns):
    dB = nx.MultiDiGraph()
    # dB.add_edge("AA","AT") # sample edge in case you want to run the code without implementing your solution
    # YOUR SOLUTION HERE
    ## BEGIN SOLUTION
    k = len(patterns[0])
    for kmer in patterns:
        prefix = kmer[:(k-1)]
        suffix = kmer[1:]
        dB.add_edge(prefix,suffix)
    ## END SOLUTION
    return dB

def eulerian_cycle(G,start=None):
    # YOUR SOLUTION HERE
    cycle = None
    ## BEGIN SOLUTION
    edges = {}
    cnt = 0
    for u,v in G.edges():
        if u not in edges:
            edges[u] = []
        edges[u].append(v)
        cnt += 1
    if start is None:
        start = list(edges.keys())[0]
    cycle = [start]
    current = start
    ecnt = 0
    while ecnt < cnt:
        while True:
            neighbors = edges[current]
            if len(neighbors) > 0:
                break
            # we need to keep shifting until we get to a point that has unused portions
            cycle = [cycle[-2]] + cycle[0:-2] + [cycle[-2]]
            current = cycle[-1]
            
        current = neighbors.pop()
        cycle.append(current)
        ecnt += 1
    while not (cycle[0] == start):
        cycle = [cycle[-2]] + cycle[0:-2] + [cycle[-2]]
    ## END SOLUTION
    return cycle

def calc_in_out(G):
    in_deg = {}
    out_deg = {}
    for u,v in G.edges():
        if v not in in_deg:
            in_deg[v] = 0
        if u not in out_deg:
            out_deg[u] = 0
        in_deg[v] += 1
        out_deg[u] += 1
    in_out = pd.Series(in_deg,name="in").to_frame().join(pd.Series(out_deg,name="out").to_frame(),how='outer')
    return in_out.fillna(0).astype(int)

def eulerian_path(G):
    # YOUR SOLUTION HERE
    path = []
    ## BEGIN SOLUTION
    in_out = calc_in_out(G)
    diff = in_out["out"] - in_out["in"]
    
    end = list(in_out.index[diff < 0])[0]
    diff = in_out["in"] - in_out["out"]
    start = list(in_out.index[diff < 0])[0]
    G2 = copy.deepcopy(G)
    G2.add_edge(end,start)
    cycle = eulerian_cycle(G2)
    while not (cycle[0] == start and cycle[-2] == end):
        cycle = [cycle[-2]] + cycle[0:-2] + [cycle[-2]]
    path = cycle[:-1]
    ## END SOLUTION
    return path

def reconstruct(kmers):
    dB = de_bruijn(kmers)
    path = eulerian_path(dB)
    text = ""
    # YOUR SOLUTION HERE
    ## BEGIN SOLUTION
    prefix = path.pop(0)
    text = [prefix]
    while len(path) > 0:
        suffix = path.pop(0)
        text.append(suffix[-1])
    text = "".join(text)
    ## END SOLUTION
    return text