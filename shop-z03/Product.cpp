#include "Product.h"
#include <iostream>
using namespace std;


Product::Product(string n, int i, Money p, int v, Date d, vector<string> c, vector<Size> a, string des){
    name = n;
    id = i;
    price = p;
    views = v;
    adding_date = d;
    categories = c;
    available_models = a;
    description = des;
}


string Product::get_name() const{
    return name;
}


void Product::set_name(string n){
    name = n;
}


int Product::get_id() const{
    return id;
}


void Product::set_id(int i){
    id = i;
}


Money Product::get_price() const{
    return price;
}


void Product::set_price(Money p){
    price = p;
}


int Product::get_views() const{
    return views;
}


void Product::set_views(int v){
    views = v;
}


void Product::views_plus(){
    views += 1;
}


Date Product::get_adding_date() const{
    return adding_date;
}


void Product::set_adding_date(Date d){
    adding_date = d;
}


bool Product::operator==(Product other)
    {
        if (id == other.id)
            return true;
        else
            return false;
    };


void Product::add_category(string cat){
    categories.push_back(cat);
}


void Product::remove_category(string cat){
    for(size_t i = 0; i < categories.size(); i++){
        if(cat == categories[i]){
            categories.erase(categories.begin()+i);
        }
    }
}


bool Product::is_in_categories(string cat){
    for(size_t i = 0; i < categories.size(); i++){
        if(strncmp(categories[i].c_str(), cat.c_str(), cat.size()) == 0){
            return true;
        }
    }
    return false;
}


vector<Size> const Product::get_models() const{
    return available_models;
}


void Product::remove_from_stock(string s, int val){
    for(int i = 0; i < available_models.size(); i++){
        if(available_models[i].size==s){
            available_models[i].amount-=val;
            return;
        }
    }
    throw except_product(model_not_in_stock);
}


vector<string> Product::get_categories(){
    return categories;
}

string Product::get_description() const
{
    return description;
}

void Product::print_cout(){
    string models = "";
    for(int i = 0; i < available_models.size(); i++){
        if(available_models[i].amount > 0){
            models += available_models[i].size;
            if (i != available_models.size()-1){
                models += ", ";
            }
        }
    }
    cout << name << endl << "Cena: " << price << endl << "Dostępne rozmiary: " << models << endl << "Wyświetlenia: " << views << endl;
    cout << "Data dodania produktu: " << adding_date << endl << "Numer referencyjny: " << id << endl;
    cout << "Opis produktu: " << endl << description << endl;
}
//popraw print