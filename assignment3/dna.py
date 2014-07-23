import MapReduce
import sys

"""
dna trimming example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence identifier
    # sequence: dna sequence
    key = record[0]
    sequence = record[1]
    mr.emit_intermediate(sequence[:-10], 1)

def reducer(sequence, list_of_values):
    # sequence: trimmed sequence
    # value: list of occurrence counts
    mr.emit(sequence)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
