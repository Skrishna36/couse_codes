import math

def f(t, y):
    return y - 0.5 * math.exp(0.5 * t) * math.sin(5 * t) + 5 * math.exp(0.5 * t) * math.cos(5 * t)

def euler1(h, t0, y0):
    y = y0
    t = t0
    
    with open("euler2.dat", "w") as fout:
        while t <= 5.0:
            exact = math.exp(0.5 * t) * math.sin(5 * t)
            
            # Print to console and file
            print(f"{t:.4f}  {y:.6f}  {exact:.6f}")
            fout.write(f"{t}  {y}  {exact}\n")
            
            # Euler update step
            y += h * f(t, y)
            t += h

if __name__ == "__main__":
    euler1(0.1, 0.0, 0.0)
