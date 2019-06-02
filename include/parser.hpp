#ifndef PARSER_HPP
#define PARSER_HPP 1

#include <algorithm>

#include "lexer.hpp"
#include "nodes.hpp"
#include "utils.hpp"

#define RESERVLEN 1

typedef std::vector<Node *> AST;

typedef struct {
    AST ast;
    Tokens * tokens;

    bool filtering;
    bool init = false;
    unsigned int position = 0;

    std::vector<std::string> reserved;
    std::vector<std::string *> filtered;
} Processor;

AST parse(Tokens tokens);

void get_next();
bool make_predict();
void update_predict();
TokenType nextType();
TokenType currentType();
std::string currentValue();
Node * instruction(std::string * instr);

#endif