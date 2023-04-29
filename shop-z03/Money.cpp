#include "Money.h"
#include <iostream>
using namespace std;


Money::Money(int z, int g){
    if (z < 0 || g < 0){
        throw negative_money;
    }
    grosze = z * 100 + g;
}


int Money::get_zloty() const{
    return grosze / 100;
}


int Money::get_grosze() const{
    return grosze % 100;
}


Money Money::operator+(Money m1){
    return Money ((grosze+m1.grosze)/100,(grosze+m1.grosze)%100);
}


Money Money::operator-(Money m1){
    if (grosze - m1.grosze < 0){
        throw negative_money;
    }
    else{ 
        return Money ((grosze-m1.grosze)/100,(grosze-m1.grosze)%100);
    }
}


bool Money::operator==(Money m1){
    return (grosze == m1.grosze);
}


bool Money::operator>(Money m1){
    return (grosze > m1.grosze);
}


bool Money::operator<(Money m1){
    return (grosze < m1.grosze);
}


void Money::print(){
    if (grosze % 100 < 10){
        cout << grosze / 100 << "," << "0" << grosze % 100 << " zł" << endl;  
    }
    else{
        cout << grosze / 100 << "," << grosze % 100 << " zł" << endl;
    }
}


string Money::money_string(){
    if (grosze % 100 < 10){
        return to_string(grosze / 100) + "," + "0" + to_string(grosze % 100) + " zł" + "\n";  
    }
    else{
        return to_string(grosze / 100) + "," + to_string(grosze % 100) + " zł" + "\n";
    }
}


ostream& operator<<(ostream& os, Money const& m){
    if (m.get_grosze() < 10){
        return os << m.get_zloty() << "," << "0" << m.get_grosze() << " zł";
    }
    else{
        return os << m.get_zloty() << "," << m.get_grosze() << " zł";
    }
}