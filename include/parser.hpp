#ifndef PARSER_HPP
#define PARSER_HPP 1

#include <vector>
#include <string>

#include "nodes.hpp"
#include "lexer.hpp"
#include "utils.hpp"
#include "reader.hpp"

typedef std::vector<Node *> AST;

AST generateAST(Tokens tokens);

void addRoot(void);

void addInstruction(std::string inst);
void addString(const std::string str);
void addNumber(const std::string str);

#endif