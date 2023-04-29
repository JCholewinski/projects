#pragma once
#include <stdexcept>
#include <iostream>

class Date
{
private:
    unsigned int day;
    unsigned int month;
    unsigned int year;

public:
    Date(unsigned int d=1, unsigned int m=1, unsigned int y=1);

    void set_day(unsigned int d)
    {
        if (d > 31 or d < 1)
        {
            throw std::out_of_range("Niepoprawny dzień!");
        }
        else
        {
            day = d;
        }
    }

    void set_month(unsigned int m)
    {
        if (m > 12 or m < 1)
            throw std::out_of_range("Niepoprawny miesiąc!");
        else
        {
            month = m;
        }
    }
    void set_year(unsigned int y)
    {
        year = y;
    }

    unsigned int get_day() const {return day;}
    unsigned int get_month() const {return month;}
    unsigned int get_year() const {return year;}

    void print_date() const;
    std::string return_date() const;
    bool operator<(const Date & dt) const;
    friend std::ostream& operator<<(std::ostream& os, Date d){
        return os << d.day << "-" << d.month << "-" << d.year;
    };
    bool operator==(const Date& dt) const;
};