# Import BioPython
from Bio.Seq import Seq
# Introduce desired sequence
MySeq = Seq("AAAACCCGGT")
# Use the Seq related function 
print(MySeq.reverse_complement())

