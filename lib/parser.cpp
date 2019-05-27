#include "parser.hpp"

AST ast;
Node * instruction;

AST generateAST(Tokens tokens)
{
    ast.clear();
    for(Token t : tokens)
    {
        switch(t.first)
        {
            case LITERAL: addInstruction(t.second); break;
            case NUMBER: break;
            case STRING: addString(t.second);       break;
            case DELIMITER: addRoot();              break;
            default: break; // TODO: Handler error
        }
    }

    return ast;
}

void addRoot(void)
{
    ast.emplace_back(instruction);
    instruction = nullptr;
}

void addInstruction(std::string inst)
{
    inst = tolower(inst);
    if(instruction == nullptr)
    {
        if(inst.compare("di") == 0) instruction = new Statement();
    }
}

void addString(const std::string str)
{
    if(instruction == nullptr) ;
    else instruction->append(new String(str));
}