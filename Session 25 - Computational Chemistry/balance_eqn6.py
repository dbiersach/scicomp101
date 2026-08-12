#!/usr/bin/env -S uv run
"""balance_eqn6.py"""

import pulp

x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")  # P2I4
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")  # P4
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")  # H2O
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")  # PH4I
x4 = pulp.LpVariable(name="x4", lowBound=1, cat="Integer")  # H3PO4

prob = pulp.LpProblem(sense=pulp.LpMinimize)
prob.name = "Equation #6"

prob += 2 * x0 + 4 * x1 == x3 + x4  # Phosphorus (P)
prob += 4 * x0 == x3  # Iodine (I)
prob += 2 * x2 == 4 * x3 + 3 * x4  # Hydrogen (H)
prob += x2 == 4 * x4  # Oxygen (O)

prob += pulp.lpSum([x0, x1, x2, x3, x4])
prob.solve(pulp.HiGHS(msg=0))

print(prob.name)
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
print(f"x4 = {pulp.value(x4):n}")
