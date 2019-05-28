#include "nodes.hpp"

// ------------------------------------------------------------------

std::unordered_map<std::string,std::any> variables;

// ------------------------------------------------------------------

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
void Print::evaluate() const {
    children.front()->evaluate();
    std::any value = variables.find(RESULT)->second;
    switch(value.type().name()[0])
    {
        case 'd': std::cout << std::any_cast<double>(value) << std::endl; break;
        case 'N': std::cout << std::any_cast<std::string>(value) << std::endl;  break;
        default: ; // TODO: Error handler
    }
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
void String::evaluate() const { variables.insert_or_assign(RESULT, str); }
std::string String::toString() const { return "<String \"" + str + "\">"; }

// ------------------------------------------------------------------

Number::Number(const double &n) : number(n) { children.reserve(0); }
void Number::evaluate() const { variables.insert_or_assign(RESULT, number); }
std::string Number::toString() const { return "<Number \"" + std::to_string(number) + "\">"; }