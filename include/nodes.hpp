#ifndef NODE_HPP
#define NODE_HPP 1

#include <tuple>
#include <vector>
#include <string>
#include <iostream>

#define NONUM 0
#define NOSTR ""

typedef std::tuple<double,std::string> result;

class Node
{
    public:
        Node() = default;
        virtual ~Node() = default;
        void append(Node * n);
        virtual result evaluate() const = 0;
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
        virtual ~Print() = default;
        virtual result evaluate() const;
        virtual std::string toString() const;
};

class String : public Node
{
    public:
        String(const std::string &s);
        virtual ~String() = default;
        virtual result evaluate() const;
        virtual std::string toString() const;
    private:
        std::string str;
};

class Number : public Node
{
    public:
        Number(const double &n);
        virtual ~Number() = default;
        virtual result evaluate() const;
        virtual std::string toString() const;
    private:
        double number;
};

#endif