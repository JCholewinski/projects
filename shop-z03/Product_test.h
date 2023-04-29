#include "Product.h"
#include <iostream>
#include <ctime>
using namespace std;

int product_test(){
    cout << "Testy klasy Product" << endl;
    Money p1(199,99);
    Date d1(5,5,2022);
    Size s1("S", 15);
    Size m1("M", 14);
    vector<string> cat1 = {"bluzka", "biała"};
    vector<Size> size1 = {s1, m1};
    Product prod1("Nike Pro - biała", 1, p1, 0, d1, cat1, size1, "Biała koszulka, 100% bawełna, idealna na lato");
    Money p2(150,0);
    Date d2(1,1,2021);
    Size s2("32", 13);
    Size m2("34", 12);
    vector<string> cat2 = {"spodnie", "jeansy", "niebieskie", "levi's"};
    vector<Size> size2 = {s2, m2};
    Product prod2("jeansy - levi's", 2, p2, 5, d2, cat2, size2, "markowe jeansy Levi's z dziurami");
    if (prod1.get_name() == "Nike Pro - biała" && prod1.get_id() == 1 && prod1.get_price().get_zloty() == 199 &&
    prod1.get_views() == 0 && prod1.get_adding_date().get_day() == 5 && prod1.is_in_categories("bluzka") &&
    prod1.get_models()[0].size == "S" && prod1.get_description() == "Biała koszulka, 100% bawełna, idealna na lato"){
        cout << "Test #1 passed!" << endl;
    }
    else {cout << "Test #1 failed!" << endl;}
    prod1.set_name("Nike air - biała");
    prod1.set_id(2);
    prod1.set_price(p2);
    prod1.set_views(10);
    prod1.views_plus();
    prod1.set_adding_date(d2);
    prod1.remove_category("biała");
    prod1.add_category("Nike");
    prod1.remove_from_stock("S", 5);
    if(prod1.get_name() == "Nike air - biała" && prod1.get_id() == 2 && prod1.get_price().get_zloty() == 150 &&
    prod1.get_views() == 11 && prod1.get_adding_date().get_day() == 1 && prod1.is_in_categories("Nike") &&
    prod1.is_in_categories("biała") == false && prod1.get_models()[0].amount == 10){
        cout << "Test #2 passed!" << endl;
    }
    else{cout << "Test #2 failed!" << endl;}
    if(prod1 == prod2){cout << "Test #3 passed!" << endl;}
    else{cout << "Test #3 failed!"<< endl;}
    bool con = true;
    try{
        prod1.remove_from_stock("L", 5);
    }
    catch (except_product){
        cout << "Test #4 passed!" << endl;
        con = false;
    }
    if (con){
        cout << "Test #4 failed!" << endl;
    }
    return 0;
}