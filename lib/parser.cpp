#include "parser.hpp"

AST root;
Node * current;
Processor processor;
std::string predict;

AST parse(Tokens tokens)
{
    predict.clear();
    processor.reserved.reserve(RESERVLEN);
    processor.reserved = { "di" };

    processor.tokens = &tokens;
    while(processor.position < processor.tokens->size())
        get_next();

    return root;
}

void get_next()
{
    if(!processor.init)
    {
        // Comprobamos que lo primero es un delimitador
        if(currentType() == DELIM)
            processor.init = true;
        else
        {
            // Handle error
        }
    } else
    {
        switch(currentType())
        {
            case LITERAL:
                update_predict();
                if(make_predict())
                    current = instruction(&predict);
                break;
            case STRING:
                if(current) // && nextType() != TokenType::BINOP)
                    current->append(new String(currentValue()));
                else
                    ; // Error Handler
                break;
            case NUMBER: break;
            case OP: break;
            case BINOP: break;
            case DELIM:
                if(current)
                    root.emplace_back(current);
                predict.clear();
                current = nullptr;
                break;
            default: break;
        }
    }

    processor.position++;
}

void update_predict()
{
    if(!predict.empty())
        predict += " ";
    predict += util::tolower(currentValue());
}

bool make_predict()
{
    bool end;
    std::vector<std::string> tmp;
    tmp.reserve(RESERVLEN);

    end = util::contains(processor.reserved, predict);
    return end;
}

Node * instruction(std::string * instr)
{
    if(instr->compare("di") == 0) return new Print();
    else return nullptr;
}

TokenType currentType()
{
    return processor.tokens->at(processor.position).first;
}

std::string currentValue()
{
    return processor.tokens->at(processor.position).second;
}

TokenType nextType()
{
    TokenType type = TokenType::UNKNOWN;
    if(processor.position + 1 < processor.tokens->size())
        type = processor.tokens->at(processor.position + 1).first;
    return type;
}

// https://mariusbancila.ro/blog/2009/02/05/evaluating-expressions-part-3-building-the-ast/