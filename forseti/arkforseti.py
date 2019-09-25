# from forseti import parser
# from forseti.formula import Predicate, And
# assert parser.parse("and(a, b)") == And(Atomic('a'), Atomic('b'))

# from forseti.prover import Prover
# prover = Prover()
# prover.add_formula("if(A,and(B,C))")
# prover.add_formula("iff(C,B)")
# prover.add_formula("not(C)")
# prover.add_goal("not(A)")
# assertTrue(prover.run_prover())

"""
A brief demonstration of using the prover within Forseti
"""
from __future__ import print_function
from forseti.prover import Prover
import time

# pylint: disable=duplicate-code
# t0 = time.time()
# prover = Prover()
# prover.add_formula("or(iff(G,H),iff(not(G),H))")
# prover.add_goal("or(iff(not(G),not(H)),not(iff(G,H)))")
# # prover.run_prover()
# prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# # print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)

# t0 = time.time()
# prover = Prover()
# prover.add_formula("and(and(if(A,and(B,C)),iff(C,B)),not(C))")
# # prover.add_formula("iff(C,B)")
# # prover.add_formula("not(C)")
# prover.add_goal("not(A)")
# # prover.run_prover()
# prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# # print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)


# t0 = time.time()
# prover = Prover()
# prover.add_formula("and(if(A,B),if(B,C))")
# # prover.add_formula("if(B,C)")
# prover.add_goal("if(A,C)")
# prover.run_prover()
# # prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# print("\n".join(prover.get_proof()))
# # print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)


# t0 = time.time()
# prover = Prover()
# prover.add_formula("not(not(A))")
# prover.add_goal("A")
# # prover.run_prover()
# prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# # print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)


# t0 = time.time()
# prover = Prover()
# prover.add_formula("not(not(or(A,B)))")
# prover.add_goal("or(A,B)")
# # prover.run_prover()
# prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# # print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)


# t0 = time.time()
# prover = Prover()
# prover.add_formula("not(not(or(A,or(B,C))))")
# prover.add_goal("or(A,or(B,C))")
# # prover.run_prover()
# prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# # print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)


# t0 = time.time()
# prover = Prover()
# prover.add_formula("not(not(or(A,or(B,or(C,D)))))")
# prover.add_goal("or(A,or(B,or(C,D)))")
# # prover.run_prover()
# prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# # print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)

# t0 = time.time()
# prover = Prover()
# prover.add_formula("not(not(or(A,or(B,or(C,or(D,E))))))")
# prover.add_goal("or(A,or(B,or(C,or(D,E))))")
# prover.run_prover()
# # prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# print("\n".join(prover.get_proof()))
# # print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)


# t0 = time.time()
# prover = Prover()
# prover.add_formula("not(not(and(A,or(B,and(C,or(D,E))))))")
# prover.add_goal("and(A,or(B,and(C,or(D,E))))")
# # prover.run_prover()
# prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# # print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)


# print("\n\n")
# t0 = time.time()
# prover = Prover()
# prover.add_formula("and(and(forall(x,if(S(x),exists(y,and(S(y),forall(z,iff(B(z,y), \
# and(B(z,x),B(z,z)))))))),forall(x,not(B(x,x)))),exists(x,S(x)))")
# # prover.add_formula("forall(x,not(B(x,x)))")
# # prover.add_formula("exists(x,S(x))")
# prover.add_goal("exists(x,and(S(x),forall(y,not(B(y,x)))))")
# # prover.run_prover()
# prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# # print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)

# t0 = time.time()
# prover = Prover()
# prover.add_formula("forall(x,if(S(x),exists(y,and(S(y),forall(z,iff(B(z,y), \
# and(B(z,x),B(z,z))))))))")
# prover.add_formula("forall(x,not(B(x,x)))")
# prover.add_formula("exists(x,S(x))")
# prover.add_goal("exists(x,and(S(x),forall(y,not(B(y,x)))))")
# prover.run_prover()
# # prover.run_prover_rev2()
# t1 = time.time()
# total = t1 - t0
# print("\n".join(prover.get_proof()))
# # print("\n".join(prover.get_proofr()))
# print("\nTime taken is", total)


t0 = time.time()
prover = Prover()
prover.add_formula("and(forall(x,if(T(x),T(a))),not(T(a)))")
# prover.add_formula("not(T(a))")
prover.add_goal("not(exists(x,T(x)))")
prover.run_prover()
# prover.run_prover_rev2()
t1 = time.time()
total = t1 - t0
print("\n".join(prover.get_proof()))
# print("\n".join(prover.get_proofr()))
print("\nTime taken is", total)

# with open('CalcRange.txt', 'w') as f:
#     f.write('{}'.format(total))

# with open('CalcRange.txt', 'a') as f:
#     f.write('\n{}'.format(total))
#
# TimeList = []
# with open('CalcRange.txt', 'r') as f:
#     for item in f:
#         TimeList.append(float(item))
#
# print('The Range is {} - {}'.format(min(TimeList), max(TimeList)))
