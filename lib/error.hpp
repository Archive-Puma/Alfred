#ifndef ERROR_HPP
#define ERROR_HPP 1

#include <string>
#include <cstdlib>
#include <iostream>

void error(std::string type, std::string msg);
void file_error(std::string file);
void alfred_error(unsigned int lineno, unsigned int linepos, std::string word);

#endif