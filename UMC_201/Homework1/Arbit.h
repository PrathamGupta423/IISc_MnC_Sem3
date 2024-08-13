#ifndef ARBIT_H
#define ARBIT_H

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

class Arbit {
private:
    std::string number;
    bool negative;

public:
    // Constructors
    Arbit();
    Arbit(const std::string& num);
    Arbit(long long num);

    // Print and toString
    std::string toString() const;
    void print() const;

};

int mod_compare(const std::string&, const std::string&);

#endif // ARBIT_H