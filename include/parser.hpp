#ifndef PARSER_HPP
#define PARSER_HPP 1

#include <list>

#include "lexer.hpp"
#include "nodes.hpp"
#include "utils.hpp"

typedef std::list<Node *> AST;

AST parse(Tokens tokens);

void set_number(std::string value);
void set_string(std::string value);

#endif