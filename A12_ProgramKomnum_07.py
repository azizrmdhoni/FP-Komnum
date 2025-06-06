import math

def ErrorApprox(x_i, x_i_1):
    return round(abs((x_i - x_i_1) / x_i) * 100, 2)

def compute_fx(x):
    x_kuadrat = x**2                  
    bagian_kali1 = -6 * x_kuadrat     
    bagian_kali2 = 19 * x
    pembilang = bagian_kali1 + bagian_kali2 + 84
    penyebut = x_kuadrat
    return round(pembilang / penyebut, 2) if penyebut != 0 else float('nan')

def printIterasi(x_prev, Iterasi):
    x_current = compute_fx(x_prev)    
    x_kuadrat = x_prev**2
    
    print(f"Iterasi {Iterasi}:")
    print(f"x{Iterasi-1} = {x_prev:.2f}")
    print(f"x{Iterasi} = ((-6)*({x_prev:.2f})² + 19 * ({x_prev:.2f}) + 84) / ({x_prev:.2f})²")
    print(f"   = ((-6) * {x_kuadrat:.2f} + {19*x_prev:.2f} + 84.00) / {x_prev**2:.2f}")
    print(f"   = ({-6*x_kuadrat:.2f} + {19*x_prev:.2f} + 84.00) / {x_prev**2:.2f}")
    print(f"   = {(-6*x_prev**2 + 19*x_prev + 84):.2f} / {x_prev**2:.2f}")
    print(f"x{Iterasi} = {x_current:.2f}")
    
    if Iterasi > 0:
        error = ErrorApprox(x_current, x_prev)
        print(f"Ea: {error}%")
    print()
    
    return x_current

def fixed_point_iterasi(initial_x, itersii):
    print("Metode Iterasi Satu Titik:")
    x = initial_x
    for i in range(1, itersii + 1):
        x = printIterasi(x, i)

fixed_point_iterasi(3.0, 5)
