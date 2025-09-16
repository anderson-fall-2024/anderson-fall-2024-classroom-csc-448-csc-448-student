dimport sys
sys.path.append(".")
sys.path.append("..")

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Topic7.joblib")
print(answers.keys())

from py448 import Topic7_helper

import numpy as np
answer_tol = 1e-10

def test_exercise_1():
    answer = Topic7_helper.trie_construction(Topic7_helper.patterns2)
    assert np.all(Topic7_helper.to_adj(answer).values == answers['answer_exercise_1'].values)

def test_exercise_2():
    trie2 = Topic7_helper.trie_construction(Topic7_helper.patterns2)
    answer = Topic7_helper.trie_matching("bananablahblahantennanabnablkjdf",trie2)
    assert np.all(tuple(answer) == tuple(answers['answer_exercise_2']))

def test_exercise_3():
    answer = Topic7_helper.suffix_trie("panamabananas$")
    assert np.all(Topic7_helper.to_adj(answer).values == answers['answer_exercise_3'].values)

def test_exercise_4():
    answer,discard = Topic7_helper.modified_suffix_trie("panamabananas$")
    assert np.all(Topic7_helper.to_adj(answer).values == answers['answer_exercise_4'].values)

def test_exercise_5():
    answer = Topic7_helper.to_adj(Topic7_helper.suffix_tree_construction("panamabananas$"))
    answer.index = [str(c) for c in answer.index]
    answer.columns = [str(c) for c in answer.columns]
    instructor_answer = answers['answer_exercise_5']
    answer_order = list(instructor_answer.index)
    answer = answer.loc[answer_order,answer_order]
    assert np.all(answer.values == instructor_answer.values)