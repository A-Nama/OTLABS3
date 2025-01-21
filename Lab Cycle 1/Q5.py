from scipy.optimize import linprog

c = [-5, -3]


A = [
    [2, 1], 
    [1, 1]
]


b = [500, 1200]


x_bounds = (100, None)
y_bounds = (50, None)

result = linprog(c, A_ub = A, b_ub = b, bounds =[x_bounds, y_bounds], method = 'highs')

if result.success:
    chocolatecakes = result.x[0]
    vanillacakes = result.x[1]
    
    max_profit = -result.fun 
    
    print(f"Optimal number of chocolate cakes: {chocolatecakes}")
    print(f"Optimal number of vanilla cakes: {vanillacakes}")
    print(f"Maximum amount of profit: ${max_profit}")
else:
    print("No solution found.")