#include "Database.h"

void Database::add_product(const Product& new_prod)
{
    for(size_t idx = 0; idx < products.size(); idx++)
    {
        if (products[idx].get_id() == new_prod.get_id())
            throw invalid_argument("This product is already added.");
    }
    products.push_back(new_prod);
}

void Database::remove_product(const int id)
{
    bool was = false;
    for (size_t idx = 0; idx < products.size(); idx++)
    {
        if (products[idx].get_id() == id)
        {
            products.erase(products.begin()+idx);
            was = true;
            break;
        }
    }
    if(not was)
        throw invalid_argument("Invalid id of product.");
}

const Product& Database::operator[](const int id)
{
    int i;
    bool res = false;
    for (size_t idx = 0; idx < products.size(); idx++)
    {
        if (products[idx].get_id() == id)
        {
            i =  idx;
            res = true;
            break;
        }
    }
    if (res == true)
        return products[i];
    else
        throw invalid_argument("There is no product of this id.");
}

void Database::search_by_name(string name)
{
    bool res = false;
    string path = "searchings.txt";
    search_results.clear();
    write_searching_to_txt(path, name);
    for (size_t idx = 0; idx < products.size(); idx++)
    {
        if (strncmp(products[idx].get_name().c_str(), name.c_str(), name.size()) == 0)
        {
            search_results.push_back(products[idx]);
            res = true;
        }
    }
    if (not res)
        throw invalid_argument("Product not found.");
}

void Database::sort_results_by_price(bool ascending)
{
    if (ascending)
    {
        sort(search_results.begin(), search_results.end(), Compare_methods::lower_price);
    }
    else
    {
        sort(search_results.begin(), search_results.end(), Compare_methods::higher_price);
    }
}

void Database::sort_results_by_views(bool ascending)
{
    if (ascending)
    {
        sort(search_results.begin(), search_results.end(), Compare_methods::less_views);
    }
    else
    {
        sort(search_results.begin(), search_results.end(), Compare_methods::more_views);
    }
}

void Database::sort_results_by_adding_date(bool ascending)
{
    if (ascending)
    {
        sort(search_results.begin(), search_results.end(), Compare_methods::earlier_added);
    }
    else
    {
        sort(search_results.begin(), search_results.end(), Compare_methods::later_added);
    }
}

void Database::search_by_category(string category)
{
    bool res;
    search_results.clear();
    for (size_t idx = 0; idx < products.size(); idx++)
    {
        if (products[idx].is_in_categories(category))
        {
            search_results.push_back(products[idx]);
            res = true;
        }
    }
    if (not res)
        throw invalid_argument("Category not found.");
}

vector<Product> Database::get_results() const
{
    return search_results;
}

vector<Order> Database::get_new_orders() const
{
    return new_orders;
}

void Database::add_new_order(const Order& new_ord)
{
    new_orders.push_back(new_ord);
}
vector<Product> Database::get_products() const
{
    return products;
}

delivery_methods Database::get_delivery_methods() const
{
    return delivery;
}

Money Database::get_free_delivery_min() const
{
    return delivery.free_delivery;
}

void Database::print_delivery_methods() const
{
    for(size_t idx = 0; idx < delivery.methods.size(); idx++)
    {
        cout << idx << ".:" << endl;
        cout << delivery.methods[idx].method << endl;
        cout << delivery.methods[idx].price << endl << endl;
    }
}
void Database::print()
{
    for (size_t idx = 0; idx < products.size(); idx++)
        {
            products[idx].print_cout();
            cout << endl;
        }
}

void Database::print_results()
{
    for (size_t idx = 0; idx < search_results.size(); idx++)
        {
            search_results[idx].print_cout();
            cout << endl;
        }
}

void Database::read_products_from_txt(string path)
{
    products.clear();
    fstream file;
    file.open(path, ios::in);
    if (file.good())
    {
        int line_number = 10;
        int number_of_delivery_methods;
        string line;
        string name;
        int id;
        Money price;
        int views;
        Date adding_date;
        vector<string> categories;
        vector<Size> available_models;
        string description;

        while(getline(file, line))
        {
        switch(line_number)
        {
            case 1:
            {
                name = line;
                break;
            }
            case 2:
            {
                id = stoi(line);
                break;
            }
            case 3:
            {
                string number;
                int zloty, grosz;
                stringstream sline(line);
                getline(sline, number, ' ');
                zloty = stoi(number);
                getline(sline, number);
                grosz = stoi(number);
                price = Money(zloty, grosz);
                break;
            }
            case 4:
            {
                views = stoi(line);
                break;
            }
            case 5:
            {
                string number;
                int d, m, y;
                stringstream sline(line);
                getline(sline, number, '-');
                d = stoi(number);
                getline(sline, number, '-');
                m = stoi(number);
                getline(sline, number);
                y = stoi(number);
                adding_date = Date(d, m, y);
                break;
            }
            case 6:
            {
                categories.clear();
                string cat;
                stringstream sline(line);
                while (getline(sline, cat, ' '))
                    categories.push_back(cat);
                break;
            }
            case 7:
            {
                string size;
                string amount;
                string str;
                vector<string> sizes;
                available_models.clear();
                stringstream sline(line);
                while (getline(sline, str, ' '))
                    sizes.push_back(str);
                for (size_t idx = 0; idx<sizes.size()/2; idx++)
                {
                    size = sizes[2*idx];
                    amount = sizes[2*idx+1];
                    available_models.push_back(Size(size, stoi(amount)));
                }
                break;
            }
            case 8:
            {
                description = line;
                break;
            }
            case 10:
            {
                string number;
                int zloty, grosz;
                stringstream sline(line);
                getline(sline, number, ' ');
                zloty = stoi(number);
                getline(sline, number);
                grosz = stoi(number);
                delivery.free_delivery = Money(zloty, grosz);
                break;
            }
            case 11:
            {
                number_of_delivery_methods = stoi(line);
                string name_delivery;
                for (int i=0; i < number_of_delivery_methods; i++)
                {
                    string dline;
                    getline(file, name_delivery);
                    getline(file, dline);
                    string number;
                    int zloty, grosz;
                    stringstream sline(dline);
                    getline(sline, number, ' ');
                    zloty = stoi(number);
                    getline(sline, number);
                    grosz = stoi(number);
                    delivery.methods.push_back(delivery_method(name_delivery, Money(zloty, grosz)));
                }
                line_number = 0;
                break;
            }
        }
        line_number++;
        if (line_number == 9)
        {
            line_number = 1;
            add_product(Product(name, id, price, views, adding_date, categories, available_models, description));
        }
        }

        file.close();
    }
    else
        throw invalid_argument("File cannot be open.");
}

void Database::write_orders_to_txt(string path)
{
    fstream file;
    file.open(path, ios::out);
    if (file.good() == true)
    {
        file << "New orders:" << endl;
        for(size_t idx; idx<new_orders.size(); idx++)
        {
            file << new_orders[idx].get_order();
        }
    }
    else
    {
        throw invalid_argument("Cannot open or create file.");
    }
}

void Database::write_searching_to_txt(string path, string name)
{
    fstream file;
    string searching;
    time_t t = time(0);
    tm* now = localtime(&t);
    Date date_of_search(now->tm_mday,(now->tm_mon + 1),(now->tm_year + 1900));
    searching = date_of_search.return_date();
    searching += ": ";
    searching += name;
    file.open(path, ios::app);
    if (file.good() == true)
    {
        file << searching << endl;
    }
    else
    {
        throw invalid_argument("Cannot open or create file.");
    }
}

void Database::write_products_to_txt(string path)
{
    fstream file;
    file.open(path, ios::out);
    if (file.good() == true)
    {
        int number_of_delivery_methods;
        string line;
        file << delivery.free_delivery.get_zloty() << " " << delivery.free_delivery.get_grosze() << endl;
        file << delivery.methods.size() << endl;
        for(size_t idx = 0; idx < delivery.methods.size(); idx++)
        {
            file << delivery.methods[idx].method << endl;
            file << delivery.methods[idx].price.get_zloty() << " " << delivery.methods[idx].price.get_grosze() << endl;
        }

        for(size_t idx = 0; idx < products.size(); idx++)
        {
            file << products[idx].get_name() << endl;
            file << products[idx].get_id() << endl;
            file << products[idx].get_price().get_zloty() << " " << products[idx].get_price().get_grosze() << endl;
            file << products[idx].get_views() << endl;
            file << products[idx].get_adding_date() << endl;
            for(size_t i = 0; i < products[idx].get_categories().size(); i++)
            {
                if (i == products[idx].get_categories().size()-1)
                    file << products[idx].get_categories()[i] << endl;
                else
                    file << products[idx].get_categories()[i] << " ";
            }
            for(size_t j = 0; j < products[idx].get_models().size(); j++)
                file << products[idx].get_models()[j].size << " " << products[idx].get_models()[j].amount << " ";
            file << "\n";
            file << products[idx].get_description() << endl;
        }
    }
    else
    {
        throw invalid_argument("Cannot open or create file.");
    }
}