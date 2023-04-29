#pragma once
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <algorithm>
#include "Order.h"
#include "Compare_methods.h"
#include "Delivery.h"
using namespace std;


class Database
{
    vector<Product> products;
    vector<Product> search_results;
    vector<Order> new_orders;
    delivery_methods delivery;
public:

    Database()
    {
        vector<Product> products;
        vector<Product> search_results;
        delivery = delivery_methods();
    }

    void add_product(const Product& new_prod);
    void remove_product(const int id);
    vector<Product> get_products() const;
    vector<Product> get_results() const;
    delivery_methods get_delivery_methods() const;
    void print_delivery_methods() const;
    vector<Order> get_new_orders() const;
    Money get_free_delivery_min() const;
    void print();
    void print_results();
    const Product& operator[](const int id);
    void add_new_order(const Order& new_ord);
    void search_by_name(string name);
    void search_by_category(string category);
    void sort_results_by_price(bool ascending);
    void sort_results_by_views(bool ascending);
    void sort_results_by_adding_date(bool ascending);
    void read_products_from_txt(string path);
    void write_products_to_txt(string path);
    void write_orders_to_txt(string path);
    void write_searching_to_txt(string path, string name);
};
