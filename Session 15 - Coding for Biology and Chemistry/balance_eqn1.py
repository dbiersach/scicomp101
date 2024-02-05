# balance_eqn1.py : HNO3 + Ca(OH)2 -> Ca(NO3)2 + H20

import pulp

# The goal is to minimize total atom count (POAC)
prob = pulp.LpProblem(sense=pulp.LpMinimize)

# Create the decision variables
# There is one variable for each term in the chemical equation
# If the chemical equation is ionic, we include one more variable to track charges
# In the balanced equation, each term coefficient must be an integer > 1
x0 = pulp.LpVariable(name="x0", lowBound=1, cat="Integer")
x1 = pulp.LpVariable(name="x1", lowBound=1, cat="Integer")
x2 = pulp.LpVariable(name="x2", lowBound=1, cat="Integer")
x3 = pulp.LpVariable(name="x3", lowBound=1, cat="Integer")
prob += x0 + x1 + x2 + x3

# Add in the constraints of the integer programming problem
# To be balanced, the # of reactants equals the # of products for each element
prob += x0 + 2 * x1 == 2 * x3  # Hydrogen (H)
prob += x0 == 2 * x2  # Nitrogen (N)
prob += 3 * x0 + 2 * x1 == 6 * x2 + x3  # Oxygen (O)
prob += x1 == x2  # Calcium (Ca)

# Use PuLP's default COIN "Branch and Cut solver" (CBC) MIP solver
# COIN-OR = Computational Infrastructure for Operations Research
# For more information, see https://www.coin-or.org
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Display the final value of the decision variables
print("Equation #1")
print(f"x0 = {pulp.value(x0):n}")
print(f"x1 = {pulp.value(x1):n}")
print(f"x2 = {pulp.value(x2):n}")
print(f"x3 = {pulp.value(x3):n}")
