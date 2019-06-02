#include "utils.hpp"

/**
 * Check if a string is a number (Spanish format)
 * 
 * @param str String to be checked
 * @return True if string is a number
 */
bool util::isnum(std::string str)
{
    return (str.find_first_not_of("0123456789,") == std::string::npos);
}

/**
 * Check if a string is a number (C-like format)
 * 
 * @param str String to be checked
 * @return True if string is a number
 */
bool util::iscnum(std::string str)
{
    return (str.find_first_not_of("0123456789.") == std::string::npos);
}

/**
 * Convert a string to lowercase
 * 
 * @param str String to be coverted
 * @return Lowercase string
 */
std::string util::tolower(std::string str)
{
    std::string lower;
    for(char c : str)
        lower.push_back(std::tolower(c));
    return lower;
}