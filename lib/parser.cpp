#include "parser.hpp"

AST ast;
Node * instruction;

AST generateAST(Tokens tokens)
{
    for(Token t : tokens)
    {
        switch(t.first)
        {
            case LITERAL: addInstruction(t.second); break;
            case NUMBER: addNumber(t.second);       break;
            case STRING: addString(t.second);       break;
            case DELIMITER: addRoot();              break;
            default: break; // TODO: Handler error
        }
    }

    return ast;
}

void addRoot(void)
{
    if(instruction)
        ast.emplace_back(instruction);
    instruction = nullptr;
}

void addInstruction(std::string inst)
{
    inst = tolower(inst);
    if(instruction == nullptr)
    {
        if(inst.compare("di") == 0) instruction = new Print();
    }
}

void addString(const std::string str)
{
    if(instruction == nullptr) ; // TODO: Error Handler
    else instruction->append(new String(str));
}

void addNumber(const std::string str)
{
    if(instruction == nullptr) ; // TODO: Error Handler
    else {
        double number = std::stod(str);
        instruction->append(new Number(number));
    }
}