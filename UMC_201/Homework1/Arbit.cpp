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
    if (num[0] == '-') {
        negative = true;
        i++;
    }
    while (i < n && num[i] == '0') {
        i++;
    }
    if (i == n) {
        number = "0";
        negative = false;
    } else {
        while (i < n && num[i] >= '0' && num[i] <= '9') {
            number.push_back(num[i]);
            i++;
        }        
    }

}

Arbit::Arbit(long long num) : Arbit(std::to_string(num)) {}

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
    for (int i = 0; i < a.size(); i++) {
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
    int i = a.size() - 1;
    int j = b.size() - 1;
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
    
    int cmp = mod_compare(a, b);
    if (cmp == 0) return "0";
    if (cmp < 0) {
        return "-" + subtract(b, a);
    }
    
    std::string result;
    int borrow = 0;
    int i = a.length() - 1;
    int j = b.length() - 1;
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

long long count_pairs(const std::vector<Arbit>& numbers, const Arbit& target) {
    std::unordered_map<std::string, long long> count;
    long long result = 0;

    Arbit temp = numbers[0];
    temp = temp - target;
    count[temp.toString()]++;

    for (int i = 1; i < numbers.size(); i++) {
        temp = numbers[i];
        int num_count = count[temp.toString()];
        result += num_count;
        temp = temp - target;
        count[temp.toString()]++;
    }
    return result;
}

long long count_pairs_file(const std::string& filename) {
    std::vector<Arbit> numbers;
    std::ifstream file
    {
        filename
    };
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return -1;
    }
    std::string line;

    std::getline(file, line);
    Arbit target(line);

    // target.print();

    std::getline(file, line);
    long long n = std::stoll(line);

    while (n--) {
        std::getline(file, line);
        numbers.push_back(Arbit(line));
    }

    file.close();

    // for (int i = 0; i < numbers.size(); i++) {
    //     numbers[i].print();
    // }

    return count_pairs(numbers, target);
}


extern "C" {
    long long count_pairs_file_c(const char* filename) {
        return count_pairs_file(filename);
    }
}