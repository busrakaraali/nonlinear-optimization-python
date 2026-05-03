import pulp
import random
import pandas as pd

#parameteers
nn = 12
m = 5
#i=range(1,12)
#j=range(1,5)

set_I = range(1, nn+1)
set_J = range(1, m+1)
#set_J =[1 , 2 , 3 , 4 , 5 ]
set_N = [n -j >= 1 for j in set_J for n in set_J]
a=[3,6,7,6,4,8,9,2,11,4,2,3]

A=[(),(1),(1),(2),(2),(2,3),(3),(5,6),(6,7),(4,5,8),(8,11),(9,10)]
P = pulp.OrderedDict({i: A[i-1] for i   in set_I})

b={(i,j): random.normalvariate(0,5) for i in set_I for j in set_J}
t = pulp.OrderedDict({i: a[i-1] for i in set_I})



U=3
# Model
Model = pulp.LpProblem(name="Binary_model", sense=pulp.LpMinimize)

# Variables from a dictionary
x= pulp.LpVariable.dicts("x", b.keys(), cat=pulp.LpBinary)
y= pulp.LpVariable.dicts("y", t.keys(), cat=pulp.LpBinary)
#y=pulp.LpVariable.dicts("z",t.keys(),cat=pulp.LpBinary)
if x==0 or y==0:
    z=0
else:
    z=1
C = pulp.LpVariable("C",cat=pulp.LpInteger)
if x==1 and y==1:
    a=2
else:
    if x==0 and y==0:
        a=0
    else:
        a=1
if y==1:
    y1=1
else:
    y1=0
# Constraints
#for n>=j+1 in set_J    
    Model += pulp.lpSum(x[i,j] for i in set_I for j in set_J) >= 1  #3#
    Model += pulp.lpSum(x[i,j] for i in set_I for j in set_J)  <=2   #4#
    Model += pulp.lpSum(x[i,j]+x[p] for i in set_I for j in set_J for p in P for n in set_J)  <= 1  #5#
    Model += (pulp.lpSum(x[i,j] for i in set_I for j in set_J)) -(1) == y1 #9#
for i in set_I:        
    Model += pulp.lpSum((y1*(0.5)* t[i])+ \
             pulp.lpSum(((x[i,j])-(y))*t[i]) for j in set_J) <= C   #6#
    Model += ((y1)-a) >= (-1.5)  #7#
    Model += ((1.5*y1)-a) <= 0  #8#
    Model += pulp.lpSum(y[i]) <= U #10#
    Model += C >= 0 #13#
#objectives
    Model += C

# Solve
Model.solve()

#printing results
opt_df = pd.DataFrame.from_dict(x, orient="index", columns = ["variable_object"])
opt_df.index = pd.MultiIndex.from_tuples(opt_df.index, names=["column_i", "column_j"])
opt_df.reset_index(inplace=True)
opt_df["solution_value"] = opt_df["variable_object"].apply(lambda item: item.varValue)