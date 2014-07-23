import MapReduce
import sys

"""
Friend Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend, person)

def reducer(person, friends):
    total = 0
    counts = {}; 
    for friend in friends:
      counts[friend] = counts.get(friend, 0) + 1
    for friend in counts.keys():
      if counts[friend] == 1: 
        mr.emit((person, friend));

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
