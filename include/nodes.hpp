#ifndef NODE_HPP
#define NODE_HPP 1

#include <vector>
#include <iostream>

class Node
{
    public:
        Node() = default;
        virtual ~Node() = default;

        void append(Node * n);
        virtual void evaluate() const = 0;
        virtual std::string toString() const = 0;
    protected:
        std::vector<Node *> children;
};

class Print : public Node
{
    public:
        Print();
        ~Print() = default;
        void evaluate() const;
        std::string toString() const;
};

#endif