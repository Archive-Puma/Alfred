#include "nodes.hpp"

void Node::append(Node * n) { children.emplace_back(n); }

// ------------------------------------------------------------------

std::string Statement::toString() const
{
    std::string str = "<Statement [ ";
    for(Node * n : children)
        str += n->toString() + " ";
    str += "]>";

    return str;
}

// ------------------------------------------------------------------
Print::Print() { children.reserve(1); }
result Print::evaluate() const {
    double number;
    std::string text;
    std::tie(number,text) = children.front()->evaluate();
    if(text.compare(NOSTR) == 0) std::cout << number << std::endl;
    else std::cout << text << std::endl;

    return result(NONUM,NOSTR);    
}
std::string Print::toString() const
{
    std::string str = "<Print [ ";
    for(Node * n : children)
        str += n->toString() + " ";
    str += "]>";

    return str;
}

// ------------------------------------------------------------------

String::String(const std::string &s) : str(s) { children.reserve(0); }
result String::evaluate() const { return result(NONUM,str); }
std::string String::toString() const { return "<String \"" + str + "\">"; }

// ------------------------------------------------------------------

Number::Number(const double &n) : number(n) { children.reserve(0); }
result Number::evaluate() const { return result(number,NOSTR); }
std::string Number::toString() const { return "<Number \"" + std::to_string(number) + "\">"; }