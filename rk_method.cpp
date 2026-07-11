#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>

using namespace std;


const double k = 150.0;
const double m = 7.2;


double f(double t, double x, double v) {
    return v;
}

double g(double t, double x, double v) {
    
    return -0.1 * v - 16.0 * x;
}


void rk4(double h, double t0, double &x0, double &v0, ofstream &fout) {
    double k1 = h * f(t0, x0, v0);
    double l1 = h * g(t0, x0, v0);
    
    double k2 = h * f(t0 + (h / 2.0), x0 + (k1 / 2.0), v0 + (l1 / 2.0));
    double l2 = h * g(t0 + (h / 2.0), x0 + (k1 / 2.0), v0 + (l1 / 2.0));
    
    double k3 = h * f(t0 + (h / 2.0), x0 + (k2 / 2.0), v0 + (l2 / 2.0));
    double l3 = h * g(t0 + (h / 2.0), x0 + (k2 / 2.0), v0 + (l2 / 2.0));
    
    double k4 = h * f(t0 + h, x0 + k3, v0 + l3);
    double l4 = h * g(t0 + h, x0 + k3, v0 + l3);
    
    
    x0 = x0 + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
    v0 = v0 + (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
    double t_next = t0 + h;
    
    
    fout << setw(8) << t_next << "  " << setw(10) << x0 << "  " << setw(10) << v0 << "\n";
    cout << setw(8) << t_next << "  " << setw(10) << x0 << "  " << setw(10) << v0 << "\n";
}

int main() {
    ofstream fout("rk2.dat");
    if (!fout) {
        cerr << "Error opening file rk2.dat!" << endl;
        return 1;
    }

  
    double x = 0.0;
    double v = 1.0;
    double dt = 0.01;
    
    cout << fixed << setprecision(6);
    fout << fixed << setprecision(6);


    for (double t = 0.0; t <= 5.0; t += dt) {
        rk4(dt, t, x, v, fout);
    }
    
    fout.close();
    return 0;
}
