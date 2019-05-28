#ifndef NODE_HPP
#define NODE_HPP 1

#include <any>
#include <vector>
#include <string>
#include <iostream>
#include <unordered_map>

#include "variables.hpp"

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

class Statement : public Node
{
    public:
        Statement() = default;
        virtual ~Statement() = default;
        virtual std::string toString() const;

};

class Print : public Node
{
    public:
        Print();
        ~Print() = default;
        void evaluate() const;
        std::string toString() const;
};

class String : public Node
{
    public:
        String(const std::string &s);
        ~String() = default;
        void evaluate() const;
        std::string toString() const;
    private:
        std::string str;
};

class Number : public Node
{
    public:
        Number(const double &n);
        ~Number() = default;
        void evaluate() const;
        std::string toString() const;
    private:
        double number;
};

#endif