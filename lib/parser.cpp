#include "parser.hpp"

AST root;
Node * current;
Processor processor;
std::string predict;

AST parse(Tokens tokens)
{
    predict.clear();
    processor.reserved.reserve(RESERVLEN);
    processor.reserved.emplace_back("di");

    processor.tokens = &tokens;
    while(processor.position < processor.tokens->size())
        get_next();

    return root;
}

void get_next()
{
    if(!processor.init)
    {
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
            case STRING: break;
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

// https://mariusbancila.ro/blog/2009/02/05/evaluating-expressions-part-3-building-the-ast/