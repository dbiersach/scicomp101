# balance_eqn6.py : P2I4 + P4 + H2O -> PH4I + H3PO4

import pulp

prob = pulp.LpProblem(sense=pulp.LpMinimize)
x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")
x4 = pulp.LpVariable(name="x4", lowBound=1, cat="Integer")
prob += x0 + x1 + x2 + x3 + x4

# TODO: Insert the constraints here





prob.solve(pulp.PULP_CBC_CMD(msg=0))

print("Equation #6:")
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
print(f"x4 = {pulp.value(x4):n}")
