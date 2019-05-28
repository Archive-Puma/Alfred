#include "parser.hpp"

AST ast;
AST parse(Tokens tokens)
{
    unsigned int level = 0;
    for(std::list<Token>::iterator it = tokens.begin(); it != tokens.end(); ++it)
    {
        std::string value(it->second);
        switch(it->first)
        {
            case NUMBER: set_number(value); break;
            case STRING: set_string(value); break;
            default: ;
        }
    }
    return ast;
}

void set_number(std::string value)
{
    double number = std::stod(value);
    ast.emplace_back(new Number(number));
}

void set_string(std::string value)
{
    ast.emplace_back(new String(value));
}