# balance_eqn4.py : Cr2O7(-2) + (H+) + H2C2O4 -> Cr(3+) + H20 + CO2

import pulp

prob = pulp.LpProblem(sense=pulp.LpMinimize)
x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")
x4 = pulp.LpVariable(name="x4", lowBound=1, cat="Integer")
x5 = pulp.LpVariable(name="x5", lowBound=1, cat="Integer")
prob += x0 + x1 + x2 + x3 + x4 + x5

prob += 2 * x0 == x3  # Chromium (Cr)
prob += 7 * x0 + 4 * x2 == x4 + 2 * x5  # Oxygen (O)
prob += x1 + 2 * x2 == 2 * x4  # Hydrogen (H)
prob += 2 * x2 == x5  # Carbon (C)
prob += -2 * x0 + x1 == 3 * x3  # Ionic Charges

prob.solve(pulp.PULP_CBC_CMD(msg=0))

print("Equation #4:")
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
print(f"x4 = {pulp.value(x4):n}")
print(f"x5 = {pulp.value(x5):n}")
