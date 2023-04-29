#pragma once
#include <iostream>
#include <memory>
#include <vector>
#include <iterator>
#include "Money.h"
#include "Delivery.h"
using namespace std;



template <typename T>
class Cart
{
    struct Elem
    {
        int value;
        string product_size;
        shared_ptr<T> product;
        Elem(shared_ptr<T> prod, string prod_size, int val):
            product(prod), product_size(prod_size), value(val){}
    };
    vector<Elem> cart;
    delivery_methods delivery;
public:
    Cart(){};
    Cart(Cart const& cart_to_copy)
    {
        cart = cart_to_copy.cart;
        delivery = cart_to_copy.delivery;
    };


    bool check_availability(shared_ptr<T> prod, string prod_size, int value)
    {
        int id;
        auto available_models = (*prod).get_models();
        for (int i=0; i < available_models.size(); i++)
            if (available_models[i].size == prod_size)
            {
                id = i;
                break;
            }
        if (value <= available_models[id].amount)
            return true;
        else
            return false;
    }


    void add_product(shared_ptr<T> prod, string prod_size, int value=1)
    {
        if (value < 1)
            throw invalid_argument("Invalid amount of product.");
        bool availability = check_availability(prod, prod_size, value);
        if (availability == true)
        {
            bool res = false;
            for(auto it = cart.begin(); it!= cart.end(); it++)
                if((*it).product == prod && (*it).product_size == prod_size)
                {
                    int total_value = (*it).value + value;
                    availability = check_availability(prod, prod_size, total_value);
                    if (availability == true)
                    {
                        (*it).value+=value;
                        res = true;
                    }
                    else
                        throw invalid_argument("Product not available in such quantity. vol2");
                }
            if (res == false)
            {
                cart.push_back(Elem(prod, prod_size, value));
            }
        }
        else
            throw invalid_argument("Product not available in such quantity.");

    };


    void delete_product(int id, int val=1)
    {
        if (id >= 0 && id < cart.size() && val >= 0)
        {
            auto it = cart.begin()+id;
            if (((*it).value-val) <= 0)
            {
                cart.erase(it);
            }
            else
                (*it).value-=val;
        }
        else
            throw invalid_argument("Invalid index.");
    };


    int get_number_of_unit()
    {
        int result = 0;
        for (auto it = cart.begin(); it != cart.end(); it++)
            result += (*it).value;
        return result;
    }


    int get_size() {return cart.size();}


    void set_delivery_methods(delivery_methods dev){delivery = dev;}


    Elem& operator[](int id)
    {
        return cart[id];
    }


    Elem const& operator[](int id) const
    {
        return cart[id];
    }


    friend ostream& operator<<(ostream& os, Cart<T> cart)
    {
        os << "Zawartość koszyka: (" << cart.get_number_of_unit() << ")\n\n\n";
        for (int i=0; i < cart.get_size(); i++)
            os  << i+1 << "." << endl << *(cart[i].product) << "Rozmiar: " << cart[i].product_size << "\nLiczba sztuk: " << cart[i].value << "\n\n";
        os << "\nŁączna kwota: " << cart.get_amount() << "\n\n";
        return os;
    }


    Money get_amount()
    {
        Money amount(0, 0);
        for (int i=0; i < get_size(); i++)
            for (int j=0; j < cart[i].value; j++)
                amount = amount + (*(cart[i].product)).get_price();
        return amount;
    }


    Money free_delivery()
    {
        Money difference = delivery.free_delivery - get_amount();
        return difference;
    }


    bool is_free_delivery()
    {
        if (get_amount() > delivery.free_delivery || get_amount() == delivery.free_delivery)
            return true;
        else
            return false;
    }


    void clean_cart()
    {
        cart.clear();
    }


    delivery_methods get_delivery_methods() const
    {
        return delivery;
    }
};
