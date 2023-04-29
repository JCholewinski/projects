#include "Product_test.h"
#include "Cart_and_Order_test.h"
#include "Database_test.h"
#include <iostream>
using namespace std;

int main(){
    product_test();
    cart_and_order_test();
    database_test();
    cout << "End of test!" << endl;
}