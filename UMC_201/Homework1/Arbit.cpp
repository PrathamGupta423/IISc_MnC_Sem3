#include "Arbit.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <fstream>


Arbit::Arbit() : number("0"), negative(false) {}

Arbit::Arbit(const std::string& num) {

    long n = num.size();
    long i = 0;
    negative = false;
    if(n == 0){
        //raise ValueError
        // I don't expect this to happen on any of the test cases because python throws exception when the string is empty. 
        // So I will just set the number to 0.
        number = "0";
        return;
    }
    while (i < n && num[i] == ' ')
    {
        i++;
    }
    
    if (num[i] == '-') {
        negative = true;
        i++;
    }
    else if(num[i] == '+' ){
        i++;
    }
    while (i < n && num[i] == '0') {
        i++;
    }
    if (i == n || (num[i] < '0' || num[i] > '9')) {
        number = "0";
        negative = false;
    } else {
        while (i < n && num[i] >= '0' && num[i] <= '9') {
            number.push_back(num[i]);
            i++;
        }
        while (i < n && num[i] == ' ') 
        {
            i++;
        }
        if(number.size() == 0){
            //raise ValueError
            // I don't expect this to happen on any of the test cases because python throws exception when the string is not a valid representation of a number. 
            // So I will just set the number to 0.
            number = "0";
            negative = false;
            return;
        }
                
    }
    // When a interger is read in python from string:
    // 1. If the string is empty, Python will raise a ValueError. 
    // 2. If the string is not a valid representation of a number, Python will raise a ValueError.
    // 3. trailing whitespaces are removed from the string.
    // 4. leading whitespaces are removed from the string.



}

Arbit::Arbit(long long num) : Arbit(std::to_string(num)) {}

Output_Values::Output_Values() : first(0), second(0) {}


void Output_Values::operator+=(const long long other) {
    // We want to store a big interger in base 10^17 using two long longs.
    // We will store the first 17 digits in the first long long and the rest in the second long long.
    // We will add the two numbers and if the second long long is greater than 10^17, we will add the carry to the first long long.

    int carry = 0;
    carry += other/100000000000000000;
    second += other%100000000000000000;
    if (second >= 100000000000000000) {
        carry += 1;
    }
    first += carry;
    second %= 100000000000000000;
}

std::string Output_Values::to_String() const {
    std::string result;
    if (first > 0) {
        result += std::to_string(first);
        std::string second_str = std::to_string(second);
        result += std::string(17 - second_str.size(), '0') + second_str;
        return result;
    }
    if (second > 0) {
        result += std::to_string(second);
        return result;
    }
    return "0";
    
}

std::string Arbit::toString() const {
    if (number == "0") return "0";
    if(negative) return "-" + number;
    return number;
}

void Arbit::print() const {
    std::cout << toString() << std::endl;
}

// Mod Compare
int mod_compare(const std::string& a, const std::string& b) {
    if (a.size() != b.size()) {
        return a.size() < b.size() ? -1 : 1;
    }
    for (long long i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return a[i] < b[i] ? -1 : 1;
        }
    }
    return 0;
}

// String Add
std::string string_add(const std::string& a, const std::string& b) {
    std::string result;
    int carry = 0;
    long long i = a.size() - 1;
    long long j = b.size() - 1;
    while (i >= 0 || j >= 0 || carry) {
        if (i >= 0) {
            carry += a[i] - '0';
            i--;
        }
        if (j >= 0) {
            carry += b[j] - '0';
            j--;
        }
        result.push_back(carry % 10 + '0');
        carry /= 10;
    }
    std::reverse(result.begin(), result.end());
    return result;
}

std::string subtract(const std::string& a, const std::string& b){
    
    // int cmp = mod_compare(a, b);
    // if (cmp == 0) return "0";
    // if (cmp < 0) {
    //     return "-" + subtract(b, a);
    // }
    
    std::string result;
    int borrow = 0;
    long long i = a.length() - 1;
    long long j = b.length() - 1;
    while (i >= 0) {
        int diff = (a[i] - '0') - borrow;
        if (j >= 0) diff -= (b[j] - '0');
        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        result.push_back(diff + '0');
        i--;
        j--;
    }
    std::reverse(result.begin(), result.end());
    return result;
}

bool Arbit::operator==(const Arbit& other) const {
    return number == other.number && negative == other.negative;
}

Arbit Arbit::operator+(const Arbit& other) const {
    if (negative == other.negative) {
        Arbit result(string_add(number, other.number));
        result.negative = negative;
        return result;
    } else {
        int cmp = mod_compare(number, other.number);
        if (cmp == 0) return Arbit();
        if (cmp < 0) {
            Arbit result(subtract(other.number, number));
            result.negative = other.negative;
            return result;
        } else {
            Arbit result(subtract(number, other.number));
            result.negative = negative;
            return result;
        }
    }
}

Arbit Arbit::operator-(const Arbit& other) const {
    if (other == Arbit())
    {
        return *this;
    }
    
    Arbit temp = other;
    temp.negative = !temp.negative;
    return *this + temp;
}

std::string count_pairs(const std::vector<Arbit>& numbers, const Arbit& target) {
    std::unordered_map<std::string, long long> count;
    Output_Values result;

    Arbit temp = numbers[0];
    temp = temp - target;
    count[temp.toString()]++;

    for (long long i = 1; i < numbers.size(); i++) {
        temp = numbers[i];
        long long num_count = count[temp.toString()];
        result += num_count;
        temp = temp - target;
        count[temp.toString()]++;
    }
    return result.to_String();
}

std::string count_pairs_file(const std::string& filename) {
    // std::vector<Arbit> numbers;
    std::ifstream file
    {
        filename
    };
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return "-1";
    }
    std::string line;

    std::getline(file, line);
    Arbit target(line);
    std::cout << "target: " << target.toString() << std::endl;    

    std::getline(file, line);
    long long n = std::stoll(line);

    Output_Values result;
    std::unordered_map<std::string, long long> count;

    if(n <= 1){
        return "0";
    }

    std::getline(file, line);
    Arbit temp(line);
    std::cout << "temp: " << temp.toString() << std::endl;

    temp = temp - target;
    count[temp.toString()]++;
    std::cout << "temp: " << temp.toString() << std::endl;
    std::cout << "count[temp.toString()]: " << count[temp.toString()] << std::endl;
    
    for (long long i = 1; i < n; i++) {
        std::getline(file, line);
        std::cout << "line: " << line << std::endl;
        Arbit temp(line);
        std::cout << "temp: " << temp.toString() << std::endl;
        long long num_count = count[temp.toString()];
        std::cout << "num_count: " << num_count << std::endl;
        result += num_count;
        temp = temp - target;
        count[temp.toString()]++;
    }

    file.close();

    return result.to_String();
    // return result.second;
}

void test_count_pairs(){
    // Simple correctness tests

    std::vector<Arbit> input_list_1 = {Arbit("1"), Arbit("2"), Arbit("3"), Arbit("4"), Arbit("5")};
    Arbit target1("1");

    if(count_pairs(input_list_1, target1) != "0"){
        std::cerr << "Test 1 failed" << std::endl;
        return;
    }

    std::vector<Arbit> input_list_2 = {Arbit("5"), Arbit("4"), Arbit("3"), Arbit("2"), Arbit("1")};
    Arbit target2("1");

    if(count_pairs(input_list_2, target2) != "4"){
        std::cerr << "Test 2 failed" << std::endl;
        return;
    }

    std::vector<Arbit> input_list_3 = {Arbit("1"), Arbit("2"), Arbit("3"), Arbit("4"), Arbit("5")};
    Arbit target3("-3");

    if(count_pairs(input_list_3, target3) != "2"){
        std::cerr << "Test 3 failed" << std::endl;
        return;
    }

    // Test with huge integers
    std::vector<Arbit> input_list_4 = {Arbit("100000000000000000002"), Arbit("100000000000000000001"), Arbit("100000000000000000000")};
    Arbit target4("1");

    if(count_pairs(input_list_4, target4) != "2"){
        std::cerr << "Test 4 failed" << std::endl;
        return;
    }

    std::cout << "All tests passed" << std::endl;

}

extern "C" {
    const char* count_pairs_file_c(const char* filename) {
        
        std::string output_str = count_pairs_file(filename);
        return output_str.c_str();
    }
}