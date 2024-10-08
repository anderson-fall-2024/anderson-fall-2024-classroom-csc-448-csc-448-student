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
    return patterns

def de_bruijn(patterns):
    dB = nx.MultiDiGraph()
    # dB.add_edge("AA","AT") # sample edge in case you want to run the code without implementing your solution
    # YOUR SOLUTION HERE
    return dB

def eulerian_cycle(G,start=None):
    # YOUR SOLUTION HERE
    cycle = None
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
    return path

def reconstruct(kmers):
    dB = de_bruijn(kmers)
    path = eulerian_path(dB)
    text = ""
    # YOUR SOLUTION HERE
    return text