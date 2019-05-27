#include "nodes.hpp"
#include <iostream>

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

result Print::evaluate() const {
    std::string value;
    std::tie(std::ignore,value) = children[0]->evaluate();
    std::cout << value << std::endl;

    return result(0,"");    
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

String::String(const std::string &s) : str(s) { }
result String::evaluate() const { return result(0,str); }
std::string String::toString() const { return "<String \"" + str + "\">"; }