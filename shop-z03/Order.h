#pragma once
#include <iostream>
#include "Cart.h"
#include "Product.h"
#include <ctime>
#include "Delivery.h"
using namespace std;

enum except_order {out_of_stock};

struct data_order{
    string name;
    string surname;
    string street;
    string city;
    string post_code;
    string telephone;
    string email;
    data_order(string n = "", string s = "", string str = "", string c = "", string p = "", string t = "", string e = ""){
        name = n;
        surname = s;
        street = str;
        city = c;
        post_code = p;
        telephone = t;
        email = e;
    }
};


class Order
{
private:
    data_order data;
    Cart<Product> cart;
    Date date_order;
    delivery_method dev;
    bool payment;
public:
    Order(){};
    Order(Cart<Product> c){
        time_t t = time(0);
        tm* now = localtime(&t);
        Date d_o(now->tm_mday,(now->tm_mon + 1),(now->tm_year + 1900));
        date_order = d_o;
        cart = c;
        payment = false;
    }
    void set_name(string n){data.name = n;}
    void set_surname(string s){data.surname = s;}
    void set_street(string str){data.street = str;}
    void set_city(string c){data.city = c;}
    void set_post_code(string p){data.post_code = p;}
    void set_telephone(string t){data.telephone = t;}
    void set_email(string e){data.email = e;}
    data_order get_data_to_delivery()const{return data;}
    Cart<Product> get_cart() const{return cart;}
    Date get_date_order() const{return date_order;}
    delivery_method get_delivery_method() const{return dev;}
    bool get_payment_status() const{return payment;}
    delivery_methods get_delivery_methods() {return cart.get_delivery_methods();}
    void set_delivery_method(int i){dev = cart.get_delivery_methods().methods[i];}
    Money get_amount_with_delivery(){
        if (cart.get_amount() > cart.get_delivery_methods().free_delivery){return cart.get_amount();}
        else {return cart.get_amount()+dev.price;}
    }
    Money pay(){
        for(int i = 0; i < cart.get_size(); i++){
            if (cart.check_availability(cart[i].product, cart[i].product_size, cart[i].value) == false){
                throw except_order(out_of_stock);
            }
        }
        for(int i = 0; i < cart.get_size(); i++){
            (*(cart[i].product)).remove_from_stock(cart[i].product_size, cart[i].value);
        }
        return get_amount_with_delivery();
    }
    void confirm_payment(bool condition){
        if(condition==false){
            for(int i = 0; i < cart.get_size(); i++){
                (*(cart[i].product)).remove_from_stock(cart[i].product_size, -cart[i].value);
            }
        }
        else{payment = condition;}
    }
    string get_order(){
        string free_delivery;
        string order_status;
        if (cart.is_free_delivery()){free_delivery = "tak";}
        else {free_delivery = "nie";}
        if(payment==true){order_status = "opłacone";}
        else{order_status = "nieopłacone";}
        string text = "Zamówione produkty:\n";
        for(int i = 0; i < cart.get_size(); i++){
            text += to_string(i+1) +". " + (*(cart[i].product)).get_name() + "  Numer referencyjny produktu:" + to_string((*(cart[i].product)).get_id()) + "  Rozmiar:" + cart[i].product_size + "  Liczba sztuk:" +  to_string(cart[i].value) + "\n";
        }
        text += "Dane do dostawy:\n" + data.name + " " + data.surname + "\n" + data.street + "\n" + data.post_code + " " + data.city + "\nTel: " + data.telephone + "\nEmail: "+ data.email + "\n";
        text += "Metoda dostawy: " + dev.method + "\n";
        text += "Darmowa dostawa: " + free_delivery + "\n";
        text += "Status zamówienia: " + order_status + "\n";
        text += "Kwota zmówienia z dostawą: " + get_amount_with_delivery().money_string();
        return text;
    }
};
