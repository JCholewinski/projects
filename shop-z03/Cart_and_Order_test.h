#include <iostream>
#include "Product.h"
#include "Cart.h"
#include "Date.h"
#include "Order.h"
using namespace std;



int cart_and_order_test()
{
    cout << "Test class Cart oraz class Order" << endl;
    // dane początkowe do testów
    vector<string> category;
    vector<Size> sizee;


    sizee.push_back(Size("S", 10));
    sizee.push_back(Size("M", 10));
    category.push_back({"ubranie"});


    Date date(1,1,1);
    Money prize(0, 0);
    Money prize1(10, 70);
    Money prize2(200, 0);
    string des("ładne");

    shared_ptr<Product> dress(new Product("summer dress", 1, prize1, 0, date, category, sizee, des));
    shared_ptr<Product> shirt(new Product("hawaii shirt", 2, prize, 0, date, category, sizee, des));
    shared_ptr<Product> skirt(new Product("midi skirt", 3, prize, 0, date, category, sizee, des));
    shared_ptr<Product> hat(new Product("cowboy hat", 4, prize2, 0, date, category, sizee, des));



    vector<delivery_method> met {delivery_method("kurier", Money(5, 5))};
    delivery_methods dev(Money(200, 0), met);

    Cart <Product> my_cart;
    my_cart.set_delivery_methods(dev);


    // test #0
    // add first product
    my_cart.add_product(dress, "S", 5);
    if (my_cart.get_number_of_unit() == 5 && my_cart.get_size() == 1)
        cout << "Test #0 passed." << endl;
    else
        cout << "Test #0 failed." << endl;


    // test #1
    // add next the same product
    my_cart.add_product(dress, "S");
    if (my_cart.get_number_of_unit() == 6 && my_cart.get_size() == 1)
        cout << "Test #1 passed." << endl;
    else
        cout << "Test #1 failed." << endl;


    // test #2
    // add product in diffrent size
    my_cart.add_product(dress, "M");
    if (my_cart.get_number_of_unit() == 7 && my_cart.get_size() == 2)
        cout << "Test #2 passed." << endl;
    else
        cout << "Test #2 failed." << endl;


    // test #3
    // add ujemna liczba
    bool i = false;
    try
    {
        my_cart.add_product(dress, "S", -1);
    }
    catch (const exception& e)
    {
        if(string(e.what()) == "Invalid amount of product.")
            i = true;
    }
    if (my_cart.get_number_of_unit() == 7 && i == true && my_cart.get_size() == 2)
        cout << "Test #3 passed." << endl;
    else
        cout << "Test #3 failed." << endl;


    // test #4
    // invalid id to delete
    i = false;
    try
    {
        my_cart.delete_product(2);
        my_cart.delete_product(7);
        my_cart.delete_product(99);
    }
    catch (const exception& e)
    {
        if(string(e.what()) == "Invalid index.")
            i = true;
    }
    if (my_cart.get_number_of_unit() == 7 && i == true && my_cart.get_size() == 2)
        cout << "Test #4 passed." << endl;
    else
        cout << "Test #4 failed." << endl;


    // test #5
    // delete product ktorego jest duzo
    my_cart.delete_product(0);
    if (my_cart.get_number_of_unit() == 6 && my_cart.get_size() == 2 && my_cart[0].value == 5)
        cout << "Test #5 passed." << endl;
    else
        cout << "Test #5 failed." << endl;


    // test #6
    // delete single product
    my_cart.delete_product(1);
    if (my_cart.get_number_of_unit() == 5 && my_cart.get_size() == 1 && my_cart[0].value == 5)
        cout << "Test #6 passed." << endl;
    else
        cout << "Test #6 failed." << endl;


    // test #7
    // delete wiecej niz jest danego produktu
    my_cart.delete_product(0, 100);
    if (my_cart.get_number_of_unit() == 0 && my_cart.get_size() == 0)
        cout << "Test #7 passed." << endl;
    else
    {
        cout << "Test #7 failed." << endl;
        cout << my_cart << endl;
    }


    my_cart.add_product(dress, "S");
    // test #8
    // delete ujemna liczba
    i = false;
    try
    {
        my_cart.delete_product(0, -1);
    }
    catch (const exception& e)
    {
        if(string(e.what()) == "Invalid index.")
            i = true;
    }
    if (my_cart.get_number_of_unit() == 1 && i == true && my_cart.get_size() == 1)
        cout << "Test #8 passed." << endl;
    else
        cout << "Test #8 failed." << endl;


    // stan koszyka w tym miejscu 0.dress "S" 1x, stan sklepu 10x
    // test #9
    // check_availability
    if (my_cart.check_availability(dress, "S", 1000) == false &&
        my_cart.check_availability(dress, "S", 1) == true &&
        my_cart.check_availability(dress, "S", 10) == true)
        cout << "Test #9 passed." << endl;
    else
        cout << "Test #9 failed." << endl;


    // test #10
    // clean cart
    my_cart.clean_cart();
    if (my_cart.get_number_of_unit() == 0 && my_cart.get_size() == 0 && my_cart.get_amount() == Money(0, 0))
        cout << "Test #10 passed." << endl;
    else
        cout << "Test #10 failed." << endl;


    // nowe dane po oczyszczeniu koszyka
    my_cart.add_product(dress, "S");
    my_cart.add_product(shirt, "S", 2);
    my_cart.add_product(skirt, "S");
    my_cart.add_product(dress, "M");
    // kolejnosc dodania
    // 0.dress "S", 1.shirt "S", 2.skirt "S", 3.dress "M"


    // test #11
    // operator []
    if (my_cart[1].product == shirt)
        cout << "Test #11 passed." << endl;
    else
        cout << "Test #11 failed." << endl;


    // test #12
    // add_product
    i = false;
    try
    {
        my_cart.add_product(dress, "S", 10);
    }
    catch (const exception& e)
    {
        if(string(e.what()) == "Product not available in such quantity. vol2")
            i = true;
    }
    if (i == true)
        cout << "Test #12 passed." << endl;
    else
        cout << "Test #12 failed." << endl;


    // test #13
    // get_amount
    // dress - 10,70zl, pozostale produkty 0,0zl
    if (my_cart.get_amount() == Money(21, 40))
        cout << "Test #13 passed." << endl;
    else
        cout << "Test #13 failed." << endl;


    // test #14
    // is_free_delivery
    if (my_cart.is_free_delivery() == false)
        cout << "Test #14 passed." << endl;
    else
        cout << "Test #14 failed." << endl;


    // test #15
    // free_delivery
    if (my_cart.free_delivery() == Money(178, 60))
        cout << "Test #15 passed." << endl;
    else
    {
        cout << "Test #15 failed." << endl;
        cout << my_cart.free_delivery() << "!=" << Money(178, 60) << endl;
    }


    my_cart.add_product(hat, "S");
    // test #16
    // is_free_delivery
    if (my_cart.is_free_delivery() == true)
        cout << "Test #16 passed." << endl;
    else
    {
        cout << "Test #16 failed." << endl;
        cout << my_cart.get_amount() << "<" << dev.free_delivery;
    }


    // test #17
    // order constructor
    Order my_order(my_cart);
    time_t t1 = time(0);
    tm* now1 = localtime(&t1);
    if(my_order.get_date_order().get_day() == now1->tm_mday)
        cout << "Test #17 passed." << endl;
    else{
        cout << "Test #17 failed." << endl;
        cout << my_order.get_date_order().get_day() << "!=" << now1->tm_mday << endl;
    }


    // test #18
    // set_delivery_method
    my_order.set_delivery_method(0);
    if(my_order.get_delivery_method().method == "kurier"){
        cout << "Test #18 passed." << endl;
    }
    else{
        cout << "Test #18 failed." << endl;
        cout << my_order.get_delivery_method().method << " != " << my_order.get_delivery_methods().methods[0].method << endl;
    }


    // test #19
    // get_amount_with_delivery
    if(my_order.get_amount_with_delivery() == Money(221, 40)){
        cout << "Test #19 passed." << endl;
    }
    else{
        cout << "Test #19 failed." << endl;
        cout << my_order.get_amount_with_delivery() << " != " << Money(221, 40) << endl;
    }


    // test #20
    // pay
    if(my_order.pay() == Money(221, 40) && (*(shirt)).get_models()[0].amount == 8){
        cout << "Test #20 passed." << endl;
    }
    else{
        cout << "Test #20 failed." << endl;
        cout << (*(shirt)).get_models()[0].amount << " != " << 6 << endl;
    }


    // test #21
    // confirm_payment - false
    my_order.confirm_payment(false);
    if((*(shirt)).get_models()[0].amount == 10){
        cout << "Test #21 passed." << endl;
    }
    else{
        cout << "Test #21 failed." << endl;
        cout << (*(shirt)).get_models()[0].amount << " != " << 10 << endl;
    }


    // test #22
    // pay - error
    (*(shirt)).remove_from_stock("S",9);
    try{
        my_order.pay();
        cout << "Test #22 failed." << endl;
    }
    catch(except_order){
        cout << "Test #22 passed." << endl;
    }
    (*(shirt)).remove_from_stock("S",-9);


    // test #23
    // confirm_payment - true
    my_order.pay();
    my_order.confirm_payment(true);
    if(my_order.get_payment_status() == true && (*(shirt)).get_models()[0].amount == 8){
        cout << "Test #23 passed." << endl;
    }
    else{
        cout << "Test #23 failed." << endl;
        cout << (*(shirt)).get_models()[0].amount << " != " << 8 << endl;
        cout << "or condition " << my_order.get_payment_status() << " != " << "1" << endl;
    }


    my_cart.clean_cart();
    // test #24
    // is_free_delivery
    if (my_cart.is_free_delivery() == false)
        cout << "Test #24 passed." << endl;
    else
    {
        cout << "Test #24 failed." << endl;
        cout << my_cart.get_amount() << "<" << dev.free_delivery;
    }


    // test #25
    // get_amount_with_delivery - under free delivery
    Cart <Product> my_cart1;
    my_cart1.set_delivery_methods(dev);
    Order my_order1(my_cart1);
    my_order1.set_delivery_method(0);
    if(my_order1.get_amount_with_delivery() == Money(5, 5)){
        cout << "Test #25 passed." << endl;
    }
    else{
        cout << "Test #25 failed." << endl;
        cout << my_order1.get_amount_with_delivery() << " != " << Money(5, 5) << endl;
    }


    return 0;
}