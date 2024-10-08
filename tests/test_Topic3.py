import sys
sys.path.append("..")

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Topic3.joblib")

# Import the student solutions
from py448 import Topic3_helper

import networkx as nx
import numpy as np

def test_exercise_1():
    r = Topic3_helper.composition(3,"TATGGGGTGC")
    assert np.all(r == answers['answer_exercise_1'])

def test_exercise_2():
    dB = Topic3_helper.de_bruijn(["AAT","ATG","ATG","ATG","CAT","CCA","GAT","GCC","GGA","GGG","GTT","TAA","TGC","TGG","TGT"])
    r = nx.adjacency_matrix(dB).todense()
    assert np.all(r == answers['answer_exercise_2'])

def test_exercise_3():
    G = nx.MultiDiGraph()
    G.add_edge(0,3)
    G.add_edge(1,0)
    G.add_edge(2,1)
    G.add_edge(2,6)
    G.add_edge(3,2)
    G.add_edge(4,2)
    G.add_edge(5,4)
    G.add_edge(6,5)
    G.add_edge(6,8)
    G.add_edge(7,9)
    G.add_edge(8,7)
    G.add_edge(9,6)

    r = tuple(Topic3_helper.eulerian_cycle(G,start=6))
    assert np.all(r == answers['answer_exercise_3'])

def test_exercise_4():
    G2 = nx.MultiDiGraph()
    G2.add_edge(0,2);G2.add_edge(1,3);G2.add_edge(2,1);G2.add_edge(3,0);G2.add_edge(3,4);G2.add_edge(6,3);G2.add_edge(6,7);G2.add_edge(7,8);G2.add_edge(8,9);G2.add_edge(9,6)
    r = tuple(Topic3_helper.eulerian_path(G2))
    assert np.all(r == answers['answer_exercise_4'])

def test_exercise_5():
    kmers = ["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"]
    r = Topic3_helper.reconstruct(kmers)
    assert np.all(r == answers['answer_exercise_5'])

#def test_exercise_8():
#    s1="CGCAACCACAGCGCGCAGGGCAGGCGCGAGCTGTCTGAGCCCCGGCCTCGGACCGCCCACTGGACTCCCGGCACGCCCGGTGCCGCCTTCCGGCTCCAGTCCCCC"
#    s2="CGCAACGGCAGCGCGCAGGGCAGGCGCGAGCTGGCCTCTGAGCCCCGGCCTCGGACCGCCCACTCCACGCCCGGCAGGCCCGGTGCCGCCTTCCGGCTCCAGTCCCCCCGC"
#    score_1,aligned_s1_1,aligned_s2_1 = Topic2_helper.align_dynamic3(s1,s2,match_score=1,mismatch_score=0,gap_score=0)
#    score_2,aligned_s1_2,aligned_s2_2 = Topic2_helper.align_dynamic3(s1,s2,match_score=2,mismatch_score=-3,gap_score=-1)
#
#    assert (score_1 == answers['answer_exercise_8'][0]) and (score_2 == answers['answer_exercise_8'][1])


