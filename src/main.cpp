#include "io.hpp"
#include "lexer.hpp"

#include <iostream>

int main(int argc, char* argv[])
{
    std::string source = readFile(argv[1]);
    lex(&source);

    return 0;
}