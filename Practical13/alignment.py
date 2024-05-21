#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   alignment.py
@Time    :   2024/05/10 05:15:02
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
from Bio.SubsMat import MatrixInfo

def read_file(file_path):
    with open(file_path,"r") as file:
        seq = ""
        for line in file:
            if line.startswith(">"):
                continue
            else:
                seq += line.strip("\n")
        return seq
    
def calculate_score(seq1,seq2):
    blosum62 = MatrixInfo.blosum62
    score = 0
    for i in range(min(len(seq1),len(seq2))):
        amino = (seq1[i],seq2[i])
        amino_reverse = (seq2[i], seq1[i])
        if blosum62.get(amino,None) == None:
            current_score = blosum62.get(amino_reverse,None)
        else:
            current_score = blosum62.get(amino, None)
        score += current_score
    return score

def calculate_similarity(seq1, seq2):
    similarity = 0
    for amino1, amino2 in zip(seq1, seq2):
        if amino1 == amino2:
            similarity += 1
    return (similarity / len(seq1)) * 100

if __name__ == "__main__":
    human = read_file("./SLC6A4_HUMAN.fa")
    mouse = read_file("./SLC6A4_MOUSE.fa")
    rat = read_file("./SLC6A4_RAT.fa")

    human_rat_score = calculate_score(human, rat)
    human_rat_similarity = calculate_similarity(human, rat)

    human_mouse_score = calculate_score(human, mouse)
    human_mouse_similarity = calculate_similarity(human, mouse)

    mouse_rat_score = calculate_score(mouse,rat)
    mouse_rat_similarity = calculate_similarity(mouse, rat)

    print(f"Human-Rat:\nScore: {human_rat_score}\nSimilarity: {human_rat_similarity} %")
    print(f"Human-Mouse:\nScore: {human_mouse_score}\nSimilarity: {human_mouse_similarity} %")
    print(f"Mouse-Rat:\nScore: {mouse_rat_score}\nSimilarity: {mouse_rat_similarity} %")