#!/usr/bin/env -S uv run
"""balance_eqn5.py"""

import pulp

x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")  # MnO4(-)
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")  # Fe(2+)
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")  # H(+)
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")  # Mn(2+)
x4 = pulp.LpVariable(name="x4", lowBound=1, cat="Integer")  # Fe(3+)
x5 = pulp.LpVariable(name="x5", lowBound=1, cat="Integer")  # H2O

prob = pulp.LpProblem(sense=pulp.LpMinimize)
prob.name = "Equation #5"

prob += x0 == x3  # Manganese (Mn)
prob += 4 * x0 == x5  # Oxygen (O)
prob += x1 == x4  # Iron (Fe)
prob += x2 == 2 * x5  # Hydrogen (H)
prob += -x0 + 2 * x1 + x2 == 2 * x3 + 3 * x4  # Ionic Charges

prob += pulp.lpSum([x0, x1, x2, x3, x4, x5])
prob.solve(pulp.HiGHS(msg=0))

print(prob.name)
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
print(f"x4 = {pulp.value(x4):n}")
print(f"x5 = {pulp.value(x5):n}")
