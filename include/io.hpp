#ifndef IO_HPP
#define IO_HPP 1

#include <string>
#include <fstream>
#include <sstream>

#include "error.hpp"
#include "lexer.hpp"
#include "parser.hpp"

void writeParseLog(AST ast);
void writeLexLog(Tokens tokens);

std::string readFile(std::string filename);
std::string readSelf(std::string filename);

#endif