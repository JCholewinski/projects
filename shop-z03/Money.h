#pragma once
#include <iostream>
using namespace std;

enum my_except_money {negative_money};

class Money
{
private:
    int grosze;
public:
    Money(int z, int g);
    Money() {};
    int get_zloty() const;
    int get_grosze() const;
    Money operator+(Money m1);
    Money operator-(Money m1);
    bool operator==(Money m1);
    bool operator>(Money m1);
    bool operator<(Money m1);
    void print();
    string money_string();
};
ostream& operator<<(ostream& os, Money const& m);