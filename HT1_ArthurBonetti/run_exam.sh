#!/usr/bin/env bash
# this idiom 2>&1 means redirect any stderr (2>) to the same place we are redirecting stdout (&1)
#--------------------------------------------------------
#Question 1
#--------------------------------------------------------
python Question_1/question_1a.py > "question_1a.txt" 2>&1
python Question_1/interactive_1a.py 
python Question_1/question_1b.py 
python Question_1/question_1c.py 
python Question_1/question_1d.py
python Question_1/question_1e.py > "question_1e.txt" 2>&1
#--------------------------------------------------------
#Question 2
#--------------------------------------------------------
python Question_2/question_2a.py > "question_2a.txt" 2>&1
python Question_2/question_2b.py > "question_2b.txt" 2>&1
python Question_2/question_2c.py > "question_2c.txt" 2>&1
#--------------------------------------------------------
#Question 3
#--------------------------------------------------------
python Question_3/question_3a.py > "question_3a.txt" 2>&1
python Question_3/question_3b.py > "question_3b.txt" 2>&1
python Question_3/question_3c.py > "question_3c.txt" 2>&1
#--------------------------------------------------------
#Question 4
#--------------------------------------------------------
python Question_4/question_4a.py > "question_4a.txt" 2>&1
python Question_4/question_4b.py > "question_4b.txt" 2>&1
python Question_4/question_4c.py > "question_4c.txt" 2>&1
python Question_4/question_4d.py > "question_4d.txt" 2>&1
python Question_4/question_4e.py > "question_4e.txt" 2>&1
