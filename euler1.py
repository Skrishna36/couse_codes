import math

def f(t, y):
    return 2 - math.exp(-4 * t) - 2 * y

def euler1(h, t0, y0):
    y = y0
    t = t0
    
    # We use a while loop to match the floating-point step iteration
    with open("euler1.dat", "w") as fout:
        while t <= 5.0:
            exact = 1 + 0.5 * math.exp(-4 * t) - 0.5 * math.exp(-2 * t)
            
            # Print to console and file
            print(f"{t:.4f}  {y:.6f}  {exact:.6f}")
            fout.write(f"{t}  {y}  {exact}\n")
            
            # Euler update step
            y += h * f(t, y)
            t += h

if __name__ == "__main__":
    euler1(0.1, 0.0, 1.0)
