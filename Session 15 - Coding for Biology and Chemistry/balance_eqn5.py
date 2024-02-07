# balance_eqn5.py : MnO4(-) + Fe(2+) + (H+) -> Mn(2+) + Fe(3+) + H20

import pulp

prob = pulp.LpProblem(sense=pulp.LpMinimize)
x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")
x4 = pulp.LpVariable(name="x4", lowBound=1, cat="Integer")
x5 = pulp.LpVariable(name="x5", lowBound=1, cat="Integer")
prob += x0 + x1 + x2 + x3 + x4 + x5

prob += x0 == x3  # Manganese (Mn)
prob += 4 * x0 == x5  # Oxygen (O)
prob += x1 == x4  # Iron (Fe)
prob += x2 == 2 * x5  # Hydrogen (H)
prob += -x0 + 2 * x1 + x2 == 2 * x3 + 3 * x4  # Ionic Charges

prob.solve(pulp.PULP_CBC_CMD(msg=0))

print("Equation #5:")
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
print(f"x4 = {pulp.value(x4):n}")
print(f"x5 = {pulp.value(x5):n}")