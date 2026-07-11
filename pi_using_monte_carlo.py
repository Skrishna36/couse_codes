import random
import time

def estimate_pi(n):
    count = 0
    
    # In Python, random is automatically seeded with system time, 
    # but we can explicitly set it to match your C++ implementation:
    random.seed(time.time())
    
    for _ in range(n):
        x = random.random()
        y = random.random()
        z = random.random()
        
        # Check if the point falls inside the unit sphere
        if (x**2 + y**2 + z**2) <= 1.0:
            count += 1
            
    # Ratio = count / n ≈ pi / 6
    return 6.0 * (count / n)

if __name__ == "__main__":
    samples = 10000000
    print(f"Estimated Pi: {estimate_pi(samples)}")
