#include "Database.h"
using namespace std;

int database_test()
{
    cout << "Test klasy Database" << endl;
    Database data;
    bool exc = false;
    bool is_good = true;
    string test_write_order_path = "Test_orders.txt";
    string write_products_path = "Products_write.txt";
    string read_products_path = "products.txt";

    // test case 1 - reading file
    try
    {
        data.read_products_from_txt("wrong_path.txt");
    }
    catch(const std::exception& e)
    {
        exc = true;
    }
    if(not exc)
    {
        std::cerr << "Error in test case 1 - exception not catch." << endl;
        is_good = false;
    }
    try
    {
        data.read_products_from_txt(read_products_path);
    }
    catch(const std::exception& e)
    {
        is_good = false;
        std::cerr << "Error in test case 1:" << e.what() << '\n';
    }

    if(not data.get_products().size() > 0)
    {
        std::cerr << "Error in test case 1 - products list should not be empty." << endl;
        is_good = false;
    }

    if (not data.get_delivery_methods().methods.size() > 0)
    {
        std::cerr << "Error in test case 1 - delivery methods list should not be empty." << endl;
        is_good = false;
    }
    if (is_good)
        cout << "Test case 1 passed." << endl;
    
    // test case 2 - adding products
    exc = false;
    Money price(50, 00);
    Date date(28, 05, 2022);
    string desc1 = "Example description";
    vector<string> categories={"bluza", "ubrania", "szara", "z kapturem"};
    Size s("S", 10);
    Size m("M", 15);
    vector<Size> a_m={s, m};
    Product prod1("bluza nike", 100, price, 0, date, categories, a_m, desc1);
    date = Date(29, 05, 2022);
    price = Money(40, 00);
    Product prod2("bluza Puma", 101, price, 3, date, categories, a_m, desc1);
    price = Money(74, 99);
    Product prod3("bluza adidas", 102, price, 5, date, categories, a_m, desc1);
    try
    {
        data.add_product(prod1);
        data.add_product(prod2);
        data.add_product(prod3);
    }
    catch(const std::exception& e)
    {
        exc = true;
        std::cerr << "Error in test case 2: " << e.what() << '\n';
    }
    if (not exc)
        cout << "Test case 2 passed." << endl;

    // test case 3 - adding same ID product
    Product duplicate_product1("bluza nike", 100, price, 0, date, categories, a_m, desc1);
    exc = false;
    try
    {
        data.add_product(duplicate_product1);
    }
    catch(const std::exception& e)
    {
        exc = true;
        std::cerr << "Test case 3 passed."  << '\n';
    }
    if (not exc)
        std::cerr << "Error in test case 3 - exception expected." << endl;
    
    // test case 4
    is_good = true;
    exc = false;
    try
    {
        data.search_by_name("bluz");
    }
    catch(const std::exception& e)
    {
        std::cerr <<"Error in test case 4: " << e.what() << '\n';
    }
    if (not (data.get_results().size() == 4))
    {
        cerr << "Error in test case 4. There are " << data.get_results().size() << " products." << endl;
        is_good = false;
    }

    try
    {
        data.search_by_name("example");
    }
    catch(const std::exception& e)
    {
        exc = true;
    }
    if (not exc)
    {
        std::cerr << "Error in test case 4 - exception expected." << endl;
        is_good = false;
    }
    if (is_good)
        cout << "Test case 4 passed." << endl;
    
    // test case 5 - search by category
    is_good = true;
    exc = false;
    try
    {
        data.search_by_category("example");
    }
    catch(const std::exception& e)
    {
        exc = true;
    }
    if (not exc)
    {
        std::cerr << "Error in test case 5 - exception expected." << endl;
        is_good = false;
    }

    try
    {
        data.search_by_category("z kapt");
    }
    catch(const std::exception& e)
    {
        std::cerr <<"Error in test case 5: " << e.what() << '\n';
    }
    if (not (data.get_results().size() == 3))
    {
       is_good = false;
       cerr << "Error in test case 5. There are " << data.get_results().size() << " products." << endl;
    }
    if (is_good)
        cout << "Test case 5 passed." << endl;
    
    // test case 5 - sort by price
    data.sort_results_by_price(true);
    if (data.get_results()[0] == prod2 && data.get_results()[1] == prod1 && data.get_results()[2] == prod3)
        cout << "Test case 5 passed." << endl;
    else
    {
        cerr << "Error in test case 5. Expected ascending price. Current order is: " << endl;
        data.print_results();
    }

    // test case 6
    data.sort_results_by_price(false);
    if (data.get_results()[0] == prod3 && data.get_results()[1] == prod1 && data.get_results()[2] == prod2)
        cout << "Test case 6 passed." << endl;
    else
    {
        cerr << "Error in test case 6. Expected descending price. Current order is: " << endl;
        data.print_results();
    }

    // test case 7 - sort by views
    data.sort_results_by_views(true);
        if (data.get_results()[0] == prod1 && data.get_results()[1] == prod2 && data.get_results()[2] == prod3)
        cout << "Test case 7 passed." << endl;
    else
    {
        cerr << "Error in test case 7. Expected ascending views. Current order is: " << endl;
        data.print_results();
    }

        // test case 8
    data.sort_results_by_views(false);
        if (data.get_results()[0] == prod3 && data.get_results()[1] == prod2 && data.get_results()[2] == prod1)
        cout << "Test case 8 passed." << endl;
    else
    {
        cerr << "Error in test case 8. Expected descending views. Current order is: " << endl;
        data.print_results();
    }

        // test case 9 - sort by date
    data.sort_results_by_adding_date(true);
        if (data.get_results()[0] == prod1)
        cout << "Test case 9 passed." << endl;
    else
    {
        cerr << "Error in test case 9. Expected ascending date. Current order is: " << endl;
        data.print_results();
    }

        // test case 10
    data.sort_results_by_adding_date(false);
    (false);
        if (data.get_results()[0] == prod3)
        cout << "Test case 10 passed." << endl;
    else
    {
        cerr << "Error in test case 10. Expected descending date. Current order is: " << endl;
        data.print_results();
    }

        // test case 11
    exc = false;
    try
    {
        data.write_orders_to_txt(test_write_order_path);
    }
    catch(const std::exception& e)
    {
        exc = true;
        std::cerr <<"Error in test case 11: " << e.what() << '\n';
    }
    if (not exc)
        cout << "Test case 11 passed." << endl;
    
    // test case 12 - write products to txt
    exc = false;
    try
    {
        data.write_products_to_txt(write_products_path);
    }
    catch(const std::exception& e)
    {
        exc = true;
        std::cerr <<"Error in test case 12: " << e.what() << '\n';
    }
    if (not exc)
        cout << "Test case 12 passed." << endl;

    // test case 13 - read from written file
    read_products_path = "Products_write.txt";
    is_good = true;
    try
    {
        data.read_products_from_txt(read_products_path);
    }
    catch(const std::exception& e)
    {
        is_good = false;
        std::cerr << "Error in test case 13:" << e.what() << '\n';
    }
    if(not data.get_products().size() > 0)
    {
        std::cerr << "Error in test case 13 - products list should not be empty." << endl;
        is_good = false;
    }
    if (not data.get_delivery_methods().methods.size() > 0)
    {
        std::cerr << "Error in test case 13 - delivery methods list should not be empty." << endl;
        is_good = false;
    }
    if (is_good)
        cout << "Test case 13 passed." << endl;

    return 0;
}

