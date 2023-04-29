#pragma once
#include <vector>
#include <iostream>
#include <cstring>
#include "Money.h"
#include "Date.h"
using namespace std;

enum except_product {model_not_in_stock};

struct Size
{
    string size;
    int amount;
    Size(string cs, int a)
    {
        size = cs;
        amount = a;
    }
};
// ostream& operator<<(ostream& os, Size si)
//     {
//         return os << "(" << si.s << "," << si.amount << ")";
//     };


class Product
{
private:
    string name;
    int id;
    Money price;
    int views;
    Date adding_date;
    vector<string> categories;
    vector<Size> available_models;
    string description;
public:
    Product(string n, int i, Money p, int v, Date d, vector<string> c, vector<Size> a, string des);
    string get_name() const;
    void set_name(string n);
    int get_id() const;
    void set_id(int i);
    Money get_price() const;
    void set_price(Money p);
    int get_views() const;
    void set_views(int v);
    void views_plus();
    Date get_adding_date() const;
    void set_adding_date(Date d);
    string get_description() const;
    bool operator==(Product other);
    void add_category(string cat);
    void remove_category(string cat);
    bool is_in_categories(string cat);
    vector<Size> const get_models() const;
    void remove_from_stock(string s, int val);
    vector<string> get_categories();
    void print_cout();
    friend ostream& operator<<(ostream& os, Product product)
    {
        os << product.name << endl << "Cena: " << product.price  << endl;
        os << "Numer referencyjny: " << product.id << endl;
        return os;
    };
};