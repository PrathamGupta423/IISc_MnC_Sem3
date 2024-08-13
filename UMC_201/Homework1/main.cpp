#include "Arbit.h"
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    // Basic Test Constructor and Print
    Arbit a("123456789012345678901234567890");
    Arbit b("-987654321098765432109876543210");
    Arbit c(123456789);

    std::cout << "a = "; a.print();
    std::cout << "b = "; b.print();
    std::cout << "c = "; c.print();


    // Big Test Constructor and Print
    std::vector<Arbit> numbers;
    numbers.push_back(Arbit());
    numbers.push_back(Arbit(""));
    numbers.push_back(Arbit("0"));
    numbers.push_back(Arbit("000"));
    numbers.push_back(Arbit("-000"));
    numbers.push_back(Arbit("-001"));
    numbers.push_back(Arbit("0001"));
    numbers.push_back(Arbit("0001  "));
    numbers.push_back(Arbit("0001  1"));
    numbers.push_back(Arbit("9999999999999999999999999999999999999999999999999999999999999999999999999999"));
    numbers.push_back(Arbit("-111111111111111111111111111111111111111111111111111111111111111111111111111111111111"));
    numbers.push_back(Arbit("101001a111"));

    for (int i = 0; i < numbers.size(); i++)
    {
        numbers[i].print();
    }
    
    return 0;
}