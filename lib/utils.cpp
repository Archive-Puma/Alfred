#include "utils.hpp"

bool isnum(std::string str)
{
    return (str.find_first_not_of("0123456789,") == std::string::npos);
}

bool iscnum(std::string str)
{
    return (str.find_first_not_of("0123456789.") == std::string::npos);
}

std::string tolower(std::string str)
{
    std::string lower;
    for(char c : str)
        lower.push_back(std::tolower(c));
    return lower;
}