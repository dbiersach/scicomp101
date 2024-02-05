# octane_combustion.py

import pulp

prob = pulp.LpProblem(sense=pulp.LpMinimize)
x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")
prob += x0 + x1 + x2 + x3

# TODO: Insert the constraints here




prob.solve(pulp.PULP_CBC_CMD(msg=0))

print("Octane Combustion Equation:")
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
