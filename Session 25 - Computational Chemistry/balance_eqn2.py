#!/usr/bin/env -S uv run
"""balance_eqn2.py"""

import pulp

x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")  # C7H6O2
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")  # O2
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")  # CO2
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")  # H20

prob = pulp.LpProblem(sense=pulp.LpMinimize)
prob.name = "Equation #2"

prob += 7 * x0 == x2  # Carbon (C)
prob += 6 * x0 == 2 * x3  # Hydrogen (H)
prob += 2 * x0 + 2 * x1 == 2 * x2 + x3  # Oxygen (O)

prob += pulp.lpSum([x0, x1, x2, x3])
print(prob)

prob.solve(pulp.HiGHS(msg=0))
print(prob.name)
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
