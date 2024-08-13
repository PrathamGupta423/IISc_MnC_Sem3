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
