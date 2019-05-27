#ifndef NODE_HPP
#define NODE_HPP 1

#include <vector>
#include <string>
#include <tuple>

typedef std::tuple<int,std::string> result;

class Node
{
    public:
        Node() = default;
        virtual ~Node() = default;
        virtual result evaluate() const = 0;
        virtual std::string toString() const = 0;
    protected:
        void append(Node * n);
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
        Print() = default;
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

#endif