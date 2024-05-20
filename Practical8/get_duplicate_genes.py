#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   get_duplicate_genes.py
@Time    :   2024/05/20 20:39:30
@Author  :   Zhu Zhouyue 
@Version :   1.0
@Contact :   zhouyue.23@intl.zju.edu.cn
@Desc    :   None
'''

# here put the import lib
import re

def extract_and_write_fasta(fasta_file_path, output_file_path):
    with open(fasta_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        writing = False
        current_gene = ''
        for line in infile:
            if line.startswith('>'):
                if writing:
                    outfile.write(f">{current_gene}\n{gene_sequence}\n")
                writing = True
                current_gene = line[1:].strip().split()[0]
                if re.search(r'\bduplication\b', line[1:].strip()):
                    gene_sequence = ''  
                else:
                    writing = False
                    continue
            elif writing:
                gene_sequence += line.strip()
                
        if writing:
            outfile.write(f">{current_gene}\n{gene_sequence}\n")


fasta_file_path = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file_path = 'duplicate_genes.fa'
extract_and_write_fasta(fasta_file_path, output_file_path)