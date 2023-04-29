class Compare_methods
{
public:
    static bool more_views(const Product& first, const Product& second)
    {
        return  first.get_views() > second.get_views();
    }

    static bool less_views(const Product& first, const Product& second)
    {
        return  first.get_views() < second.get_views();
    }
    
    static bool lower_price(const Product& first, const Product& second)
    {
        return  first.get_price() < second.get_price();
    }
    
    static bool higher_price(const Product& first, const Product& second)
    {
        return  first.get_price() > second.get_price();
    }
    
    static bool earlier_added(const Product& first, const Product& second)
    {
        return  first.get_adding_date() < second.get_adding_date();
    }
    
    static bool later_added(const Product& first, const Product& second)
    {
        if (first.get_adding_date() == second.get_adding_date())
            return false;
        return earlier_added(second, first);
    }

};