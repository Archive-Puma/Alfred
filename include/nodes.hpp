#ifndef NODE_HPP
#define NODE_HPP 1

#include <vector>
#include <string>

class Node
{
    public:
        Node() = default;
        virtual ~Node() = default;
        virtual std::string toString() const = 0;

        void append(Node * n);
    protected:
        std::vector<Node *> children;
};

class Statement : public Node
{
    public:
        Statement() = default;
        Statement(Node * n);
        virtual ~Statement() = default;
        virtual std::string toString() const;
};

class String : public Node
{
    public:
        String(const std::string &s);
        virtual ~String() = default;

        virtual std::string toString() const;
    private:
        std::string str;
};

#endif