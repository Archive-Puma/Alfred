#ifndef UTILS_HPP
#define UTILS_HPP 1

#include <string>
#include <locale>

namespace util
{
    bool isnum(std::string str);
    bool iscnum(std::string str);
    std::string tolower(std::string str);

    // https://codereview.stackexchange.com/questions/59997/contains-algorithm-for-stdvector
    template<class C, class T>
    auto contains(const C& v, const T& x)
    -> decltype(end(v), true)
    {
        return end(v) != std::find(begin(v), end(v), x);
    }
}

#endif