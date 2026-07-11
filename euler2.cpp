#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
ofstream fout("euler2.dat");
double N=500, h=0.1;
double f(double t, double y){
return y-0.5*exp(0.5*t)*sin(5*t)+5*exp(0.5*t)*cos(5*t); }
void euler1(double h, double t0, double y0){
double y=y0;
for (double t=t0;t<=5.0; t+=h){
fout<<t<<"  "<<y<<"  "<<(exp(0.5*t)*sin(5*t))<<endl;
y+=h*f(t,y); }
}
int main(){
euler1(0.1,0.0,0.0);
return 0;
}
