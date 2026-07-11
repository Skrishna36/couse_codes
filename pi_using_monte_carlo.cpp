#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

double estimate_pi(int N) {
    double count = 0;
    double x = 0.0, y = 0.0, z = 0.0;

    // Seed the random number generator with current time
    srand(time(NULL)); 

    for (int i = 1; i <= N; i++) {
        x = (double)rand() / (double)RAND_MAX;
        y = (double)rand() / (double)RAND_MAX;
        z = (double)rand() / (double)RAND_MAX;

        // Check if the point falls inside the unit sphere
        if ((x*x + y*y + z*z) <= 1.0) {
            count++;
        }
    }

    // Ratio = count / N ≈ pi / 6
    return 6.0 * (count / (double)N);
}

int main() {
    int samples = 100000000; // Increased sample size for better precision
    cout << "Estimated Pi: " << estimate_pi(samples) << endl;
    return 0;
}
