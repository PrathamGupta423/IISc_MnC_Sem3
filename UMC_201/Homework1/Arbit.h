#ifndef ARBIT_H
#define ARBIT_H

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

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

    // Arithmetic operations
    Arbit operator+(const Arbit& other) const;
    Arbit operator-(const Arbit& other) const;

    // Comparison operations
    bool operator==(const Arbit& other) const;

};

class Output_Values {
    public:
        long long first;
        long long second;

    public:
        Output_Values();

        void operator+=(const long long other);
        std::string to_String() const;
};


int mod_compare(const std::string&, const std::string&);
std::string string_add(const std::string&, const std::string&);
std::string subtract(const std::string&, const std::string&);

std::string count_pairs(const std::vector<Arbit>&, const Arbit&);
std::string count_pairs_file(const std::string& filename);
void test_count_pairs();

extern "C" const char* count_pairs_file_c(const char*);

#endif // ARBIT_H