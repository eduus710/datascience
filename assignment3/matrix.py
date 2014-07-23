import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(value):
#	value is ("a", i, j, a_ij) or ("b", j, k, b_jk)
    if value[0] == "a":
        i = value[1]
        j = value[2]
        a_ij = value[3]
        for k in range(5):
            mr.emit_intermediate((i, k), ("a", j, a_ij))
    else:
        j = value[1]
        k = value[2]
        b_jk = value[3]
        for i in range(5):
            mr.emit_intermediate((i, k), ("b", j, b_jk))

def reducer(key, values):
# 	key is (i, k)
#	values is a list of ("a", j, a_ij) and ("b", j, b_jk)
    hash_A = {j: a_ij for (x, j, a_ij) in values if x == "a"}
    hash_B = {j: b_jk for (x, j, b_jk) in values if x == "b"}
    result = 0
    for j in range(5):
        result += hash_A.get(j, 0) * hash_B.get(j, 0)
    mr.emit((key[0],key[1],result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
