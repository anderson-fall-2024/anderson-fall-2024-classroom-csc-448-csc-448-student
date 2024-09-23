import sys
import os
sys.path.append("..")

import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib 
answers = joblib.load(str(DIR)+"/answers_Assignment1.joblib")

# Import the student solutions
import py448

import numpy as np
np.random.seed(1)
c = np.random.rand(6,4)

def test_exercise_1():
    assert np.all(answers['exercise_1'] == py448.misc.exercise_1())

def test_exercise_2():
    assert np.all(answers['exercise_2'] == py448.misc.exercise_2())

def test_exercise_3():
    assert answers['exercise_3'] == py448.misc.exercise_3(c)

def test_exercise_4():
    one,two = py448.misc.exercise_4(c)
    assert np.all(answers['exercise_4'][0] == one) and np.all(answers['exercise_4'][1] == two)
    
def test_exercise_5():
    b = py448.misc.exercise_2()
    one,two = py448.misc.exercise_5(b)
    assert np.all(answers['exercise_5'][0] == one) and np.all(answers['exercise_5'][1] == two)
    
def test_exercise_6():
    assert np.all(answers['exercise_6'] == py448.misc.exercise_6())

def test_exercise_7():
    assert np.all(answers['exercise_7'] == py448.misc.exercise_7())
