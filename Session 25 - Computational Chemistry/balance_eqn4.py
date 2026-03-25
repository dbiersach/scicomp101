#!/usr/bin/env -S uv run
"""balance_eqn4.py"""

import pulp

x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")  # Cr2O7(2-)
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")  # H(+)
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")  # H2C2O4
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")  # Cr(3+)
x4 = pulp.LpVariable(name="x4", lowBound=1, cat="Integer")  # H2O
x5 = pulp.LpVariable(name="x5", lowBound=1, cat="Integer")  # CO2

prob = pulp.LpProblem(sense=pulp.LpMinimize)
prob.name = "Equation #4"

prob += 2 * x0 == x3  # Chromium (Cr)
prob += 7 * x0 + 4 * x2 == x4 + 2 * x5  # Oxygen (O)
prob += x1 + 2 * x2 == 2 * x4  # Hydrogen (H)
prob += 2 * x2 == x5  # Carbon (C)
prob += -2 * x0 + x1 == 3 * x3  # Ionic Charges

prob += pulp.lpSum([x0, x1, x2, x3, x4, x5])
prob.solve(pulp.HiGHS(msg=0))

print(prob.name)
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
print(f"x4 = {pulp.value(x4):n}")
print(f"x5 = {pulp.value(x5):n}")
