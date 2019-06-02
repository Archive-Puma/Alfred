#include "nodes.hpp"

/**
 * * NODE *
 * 
 * append
 *      Append a Node as a child
 *      @param n The new child
 */
void Node::append(Node * n) { children.emplace_back(n); }

/**
 * * PRINT *
 * 
 * constructor
 *      Create a new Print Node with only 1 children.
 * evaluate
 *      Print the result of evaluate his child
 * toString
 *      Return the plain text representation of the current Node
 *      @return A string with a Node representation
 */
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

/**
 * * STRING *
 * 
 * constructor
 *      Create a new String Node with only no children.
 * evaluate
 *      Return the string as last evaluate value
 * toString
 *      Return the plain text representation of the current Node
 *      @return A string with a Node representation
 */
String::String(const std::string &s) : str(s) { children.reserve(0); }
void String::evaluate() const { std::cout << "STR" << std::endl; } // variables.insert_or_assign(RESULT, str); }
std::string String::toString() const { return "<String \"" + str + "\">"; }