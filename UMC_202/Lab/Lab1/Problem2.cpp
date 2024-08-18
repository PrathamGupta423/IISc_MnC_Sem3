// To-do Use fixed point iteration method to determine a solution accurate to 1e-2 for
// f(x) = x^4 - 3x^2 - 3 = 0 in interval [1,2] , with intial guess p0 = 1

#include <iostream>
#include <cmath>

using namespace std;

double f(double x) {
    return x*x*x*x - 3*x*x - 3;
}

double g(double x) {
    return pow(3*x*x + 3, 0.25);
}

double fixedPointIteration(double p0, double tol, int maxIter = 100) {
    double p;
    int i = 0;
    int n = 100;
    while (i < n) {
        p = g(p0);
        if (abs(p - p0) < tol) {
            break;
        }
        p0 = p;
        i++;
    }
    cout << "Number of iterations: " << i << endl;
    return p;
}

int main() {
    double p0, tol;
    p0 = 1;
    tol = 1e-2;
    cout << "Root of f(x) = x^4 - 3x^2 - 3 = 0 in the interval [1, 2] is: " << fixedPointIteration(p0, tol) << endl;

    return 0;
}

