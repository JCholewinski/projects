#pragma once
#include "Money.h"
#include <iostream>
#include <vector>


struct delivery_method
{
    std::string method;
    Money price;
    delivery_method(std::string met, Money pr)
    {
        method = met;
        price = pr;
    }
    delivery_method(){}
};


struct delivery_methods
{
    Money free_delivery;
    std::vector<delivery_method> methods;
    delivery_methods(Money fd, std::vector<delivery_method> met)
    {
        free_delivery = fd;
        methods = met;
    }
    delivery_methods(){}
};