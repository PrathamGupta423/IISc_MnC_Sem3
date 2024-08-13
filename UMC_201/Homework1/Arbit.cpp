#include "Arbit.h"

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
    // result.erase(0, std::min(result.find_first_not_of('0'), result.size() - 1));
    // return result.empty() ? "0" : result;
    return result;
}
