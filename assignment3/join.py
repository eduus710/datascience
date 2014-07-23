import MapReduce
import sys

"""
Inverted Index example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    for r1 in list_of_values:
      if r1[0] == 'order':
        for r2 in list_of_values:
          if r2[0] != 'order':
            mr.emit(r1+r2);

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
