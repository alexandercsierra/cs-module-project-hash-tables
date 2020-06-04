"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

from itertools import combinations
from itertools import permutations

#q = set(range(1, 10))
#q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)
q= (1, 2, 3, 4)


def f(x):
    return x * 4 + 6

# Your code here
# def sumdiff(q):


#     perm = list(permutations(q,4))
#     for i in perm:
#         if i[0] + i[1] == i[2] - i[3]:
#             print(i)

    

# sumdiff(q)
# sum_cache = {}
# diff_cache= {}


# def sumdiff(q):
#     for i in range (len(q)):
#         for j in range (len(q)):
#             print(q[i]+q[j])
#             the_sum = q[i]+q[j]
#             diff = q[i]-q[j]
#             if the_sum not in sum_cache:
#                 sum_cache[the_sum] = []
#             sum_cache[the_sum].append((q[i], q[j]))
#             if diff not in diff_cache:
#                 diff_cache[diff] = []
#             diff_cache[diff].append((q[i], q[j]))

#     sum_keys = list(sum_cache.keys())
#     diff_keys = list(diff_cache.keys())

#     i_keys = sum_keys
#     j_keys = diff_keys

#     if len(sum_keys) >= len(diff_keys):
#         i_keys = diff_keys
#         j_keys = sum_keys
   
#     dups = []
#     for i in i_keys:
#         if i_keys[i] in j_keys:
#             dups.append(i_keys[i])
    
#     if len(dups) == 0:
#         return None
#     sum_combos = []
#     diff_combos = []
#     print('dups', dups)
#     print('sum_cache', sum_cache)
#     for num in dups:
#         sum_combos = sum_cache[num]
#         diff_combos = diff_cache[num]

    
    

# print(sumdiff(q))


def find_all_combos(arr, c=[]):
  if len(c) == len(arr):
    yield list(zip(c, arr))
  else:
    for i in arr:
       yield from find_all_combos(arr, c+[i])

print(list(find_all_combos(q)))


