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
std::string String::toString() const { return "<String \"" + str + "\">"; }