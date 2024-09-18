import pulp
import random
import sys
sys.setrecursionlimit(1000000) #例如这里设置为十万


prob = pulp.LpProblem("ExperAllocation",pulp.LpMinimize)
N = 125
M = 3000
K = 5

X = pulp.LpVariable.dicts("ExpertAssignment",((i,j) for i in range(N) for j in range (M)),0,1,pulp.LpBinary)
C = {(i,j):random.random() for i in range(N) for j in range(M)}
prob += pulp.lpSum(X[i,j]*C[i,j] for i in range(N) for j in range(M))

print("prob初始化")

for j in range(M):
    prob += pulp.lpSum(X[i,j] for i in range(N))==K
    # print(prob)
for i in range(N):
    prob += pulp.lpSum(X[i,j]for j in range(M)) <= 1

prob.solve()
print("Status:",pulp.LpStatus[prob.status])
for v in prob.variables():
    print(v.name,"=",v.varValue)
print("F(x)=",pulp.value(prob.objective))

