#!/usr/bin/env -S uv run
"""balance_eqn1.py"""

import pulp  # Python Linear Programming package

x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")  # HNO3
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")  # Ca(OH)2
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")  # Ca(NO3)2
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")  # H20

prob = pulp.LpProblem(sense=pulp.LpMinimize)
prob.name = "Equation #1"

prob += x0 + 2 * x1 == 2 * x3  # Hydrogen (H)
prob += x0 == 2 * x2  # Nitrogen (N)
prob += 3 * x0 + 2 * x1 == 6 * x2 + x3  # Oxygen (O)
prob += x1 == x2  # Calcium (Ca)

prob += pulp.lpSum([x0, x1, x2, x3])
print(prob)

prob.solve(pulp.HiGHS(msg=0))
print(prob.name)
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
