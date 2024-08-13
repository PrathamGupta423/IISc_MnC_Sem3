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

    std::cout<<"--------------------------------"<<std::endl;

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

    std::cout<<"--------------------------------"<<std::endl;
    
    // Test Mod Compare
    std::cout << mod_compare("123", "123") << std::endl;
    std::cout << mod_compare("123", "124") << std::endl;
    std::cout << mod_compare("124", "123") << std::endl;
    std::cout << mod_compare("123", "1234") << std::endl;
    std::cout << mod_compare("1234", "123") << std::endl;
    std::cout << mod_compare("1234", "1235") << std::endl;
    std::cout << mod_compare("323", "1234") << std::endl;
    std::cout << mod_compare("123", "323") << std::endl;

    std::cout<<"--------------------------------"<<std::endl;

    // Test String Add
    std::cout << string_add("123", "123") << std::endl;
    std::cout << string_add("123", "124") << std::endl;
    std::cout << string_add("124", "123") << std::endl;
    std::cout << string_add("123", "1234") << std::endl;
    std::cout << string_add("1234", "123") << std::endl;
    std::cout << string_add("1234", "1235") << std::endl;
    std::cout << string_add("323", "1234") << std::endl;
    std::cout << string_add("123", "323") << std::endl;
    std::cout << string_add("99999", "9999") << std::endl;
    std::cout<<"--------------------------------"<<std::endl;

    // Test Subtract
    std::cout << subtract("123", "123") << std::endl;
    std::cout << subtract("123", "124") << std::endl;
    std::cout << subtract("124", "123") << std::endl;
    std::cout << subtract("123", "1234") << std::endl;
    std::cout << subtract("1234", "123") << std::endl;
    std::cout << subtract("1234", "1235") << std::endl;
    std::cout << subtract("323", "1234") << std::endl;
    std::cout << subtract("123", "323") << std::endl;

    std::cout<<"--------------------------------"<<std::endl;

    // Test Addition
    Arbit sum = Arbit() + Arbit();
    std::cout << "0 + 0 = "; sum.print();
    sum = Arbit("123") + Arbit("123");
    std::cout << "123 + 123 = "; sum.print();
    sum = Arbit("123") + Arbit("124");
    std::cout << "123 + 124 = "; sum.print();
    sum = Arbit("999") + Arbit("999");
    std::cout << "999 + 999 = "; sum.print();
    sum = Arbit("999") + Arbit("1");
    std::cout << "999 + 1 = "; sum.print();
    sum = Arbit("0") + Arbit("999");
    std::cout << "0 + 999 = "; sum.print();
    sum = Arbit("999") + Arbit("0");
    std::cout << "999 + 0 = "; sum.print();
    sum = Arbit("999") + Arbit("-999");
    std::cout << "999 + -999 = "; sum.print();
    sum = Arbit("-999") + Arbit("999");
    std::cout << "-999 + 999 = "; sum.print();
    sum = Arbit("-999") + Arbit("-999");
    std::cout << "-999 + -999 = "; sum.print();
    sum = Arbit("999") + Arbit("-1000");
    std::cout << "999 + -1000 = "; sum.print();
    sum = Arbit("-1000") + Arbit("999");
    std::cout << "-1000 + 999 = "; sum.print();
    sum = Arbit("-1000") + Arbit("-999");
    std::cout << "-1000 + -999 = "; sum.print();
    sum = Arbit("-999") + Arbit("-0000");
    std::cout << "-999 + -0000 = "; sum.print();

    std::cout<<"--------------------------------"<<std::endl;

    // Test Subtraction
    Arbit diff = Arbit() - Arbit();
    std::cout << "0 - 0 = "; diff.print();
    diff = Arbit("123") - Arbit("123");
    std::cout << "123 - 123 = "; diff.print();
    diff = Arbit("123") - Arbit("124");
    std::cout << "123 - 124 = "; diff.print();
    diff = Arbit("999") - Arbit("999");
    std::cout << "999 - 999 = "; diff.print();
    diff = Arbit("999") - Arbit("1");
    std::cout << "999 - 1 = "; diff.print(); 
    diff = Arbit("0") - Arbit("999");
    std::cout << "0 - 999 = "; diff.print();
    diff = Arbit("999") - Arbit("0");
    std::cout << "999 - 0 = "; diff.print();
    diff = Arbit("999") - Arbit("-999");
    std::cout << "999 - -999 = "; diff.print();
    diff = Arbit("-999") - Arbit("999");
    std::cout << "-999 - 999 = "; diff.print();
    diff = Arbit("-999") - Arbit("-999");
    std::cout << "-999 - -999 = "; diff.print();
    diff = Arbit("999") - Arbit("-1000");
    std::cout << "999 - -1000 = "; diff.print();
    diff = Arbit("1000") - Arbit("-0");
    std::cout << "1000 - -0 = "; diff.print();
        
    return 0;
}