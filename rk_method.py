import math

# System parameters matching your C++ global variables
k = 150.0
m = 7.2
dt = 0.01

# System of first-order ODEs
def f(t, x, v):
    return v

def g(t, x, v):
    # Damped harmonic oscillator equation: -0.1*v - 16*x
    return -0.1 * v - 16.0 * x

def rk4_step(h, t0, x0, v0):
    k1 = h * f(t0, x0, v0)
    l1 = h * g(t0, x0, v0)
    
    k2 = h * f(t0 + h/2.0, x0 + k1/2.0, v0 + l1/2.0)
    l2 = h * g(t0 + h/2.0, x0 + k1/2.0, v0 + l1/2.0)
    
    k3 = h * f(t0 + h/2.0, x0 + k2/2.0, v0 + l2/2.0)
    l3 = h * g(t0 + h/2.0, x0 + k2/2.0, v0 + l2/2.0)
    
    k4 = h * f(t0 + h, x0 + k3, v0 + l3)
    l4 = h * g(t0 + h, x0 + k3, v0 + l3)
    
    # Compute the weighted average step updates
    next_x = x0 + (k1 + 2.0*k2 + 2.0*k3 + k4) / 6.0
    next_v = v0 + (l1 + 2.0*l2 + 2.0*l3 + l4) / 6.0
    next_t = t0 + h
    
    return next_t, next_x, next_v

if __name__ == "__main__":
    # Initial conditions
    x = 0.0
    v = 1.0
    t = 0.0
    t_max = 5.0
    
    # Open a data file for writing ("w" mode creates/overwrites the file)
    with open("rk2.dat", "w") as fout:
        # Loop matching the C++ main loop execution structure
        while t <= t_max:
            # Unpack the returned values to properly step forward in time
            t_next, x_next, v_next = rk4_step(dt, t, x, v)
            
            # Print to console and log to file
            output_line = f"{t_next:<8.4f}  {x_next:<10.6f}  {v_next:<10.6f}"
            print(output_line)
            fout.write(output_line + "\n")
            
            # Step forward
            t, x, v = t_next, x_next, v_next
