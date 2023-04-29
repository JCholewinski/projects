#include "Date.h"


Date::Date(unsigned int d, unsigned int m, unsigned int y)
{
    if (d > 31 or d < 1)
    {
        throw std::out_of_range("Niepoprawny dzień!");
    }
    else
    {
        day = d;
    }
    if (m > 12 or m < 1)
        throw std::out_of_range("Niepoprawny miesiąc!");
    else
    {
        month = m;
    }
    year = y;
}

void Date::print_date() const
{
    std::cout << day << "-" << month << "-" << year << std::endl;
}

std::string Date::return_date() const
{
    return  std::to_string(day) + "-" + std::to_string(month) + "-" + std::to_string(year);
}

bool Date::operator<(const Date & dt) const
{
    if (year != dt.year)
        return (year < dt.year);
    else if (month != dt.month)
        return (month < dt.month);
    else
        return (day < dt.day);
}

bool Date::operator==(const Date& dt) const
{
    return (year == dt.year && month == dt.month && day == dt.day);
}

