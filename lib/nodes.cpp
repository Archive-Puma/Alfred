#include "nodes.hpp"

void Node::append(Node * n) { children.emplace_back(n); }

// --

Print::Print() { children.reserve(1); }
void Print::evaluate() const
{
    std::cout << "PRINT" << std::endl;
}
std::string Print::toString() const
{
    std::string str = "<Print [ ";
    for(Node * n : children)
        str += n->toString() + " ";
    str += "]>";

    return str;
}

// --


String::String(const std::string &s) : str(s) { children.reserve(0); }
void String::evaluate() const { std::cout << "STR" << std::endl; } // variables.insert_or_assign(RESULT, str); }
std::string String::toString() const { return "<String \"" + str + "\">"; }