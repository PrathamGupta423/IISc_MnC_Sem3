// To use bisection method to find the root of a function f(x) = x^3 - 7x^2 + 14x - 6 on the intervals

// [0, 1]
// [1, 3.2]
// [3.2, 4]

// tolerance = 10e-4

#include <iostream>
#include <cmath>

using namespace std;

long double f(long double x) {
    return pow(x,3) - 7*pow(x,2) + 14*x - 6;
}

long double bisection(long double a, long double b, long double tol, int maxIter = 100) {
    long double c;
    int i = 0;
    while ((b - a) / 2 > tol && i < maxIter) {
        i++;
        c = a + (b - a) / 2;
        cout << "iteration: " << i << " c: " << c << " f(c): " << f(c) << endl;
        if (f(c) == 0) {
            return c;
        } else if (f(c) * f(a) < 0) {
            b = c;
        } else {
            a = c;
        }

    }
    c = (a + b) / 2;
    return c;

}

int main() {
    long double a, b, tol;
    a = 0;
    b = 1;
    tol = 1e-4;
    cout << "Root of f(x) = x^3 - 7x^2 + 14x - 6 on the interval [0, 1] is: " << bisection(a, b, tol) << endl;

    a = 1;
    b = 3.2;
    cout << "Root of f(x) = x^3 - 7x^2 + 14x - 6 on the interval [1, 3.2] is: " << bisection(a, b, tol) << endl;

    a = 3.2;
    b = 4;
    cout << "Root of f(x) = x^3 - 7x^2 + 14x - 6 on the interval [3.2, 4] is: " << bisection(a, b, tol) << endl;

    return 0;
}
