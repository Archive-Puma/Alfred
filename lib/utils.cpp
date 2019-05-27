#include "utils.hpp"

std::string tolower(std::string str)
{
    std::string lower;
    for(char c : str)
        lower.push_back(std::tolower(c));
    return lower;
}