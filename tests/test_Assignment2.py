import sys
sys.path.append("..")

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Assignment2.joblib")

# Import the student solutions
from py448 import Assignment2_helper

def test_exercise_1():
    s1="CGCAACCACAGCGCGCAGGGCAGGCGCGAGCTGTCTGAGCCCCGGCCTCGGACCGCCCACTGGACTCCCGGCACGCCCGGTGCCGCCTTCCGGCTCCAGTCCCCC"
    s2="CGCAACGGCAGCGCGCAGGGCAGGCGCGAGCTGGCCTCTGAGCCCCGGCCTCGGACCGCCCACTCCACGCCCGGCAGGCCCGGTGCCGCCTTCCGGCTCCAGTCCCCCCGC"
    score_1,aligned_s1_1,aligned_s2_1 = Assignment2_helper.align_dynamic3(s1,s2,match_score=1,mismatch_score=0,gap_score=0)
    score_2,aligned_s1_2,aligned_s2_2 = Assignment2_helper.align_dynamic3(s1,s2,match_score=2,mismatch_score=-3,gap_score=-1)

    assert (score_1 == answers['answer_exercise_1'][0]) and (score_2 == answers['answer_exercise_1'][1])