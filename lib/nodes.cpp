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