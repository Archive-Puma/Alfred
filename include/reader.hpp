#ifndef READER_HPP
#define READER_HPP 1

#include <string>

typedef struct {
    unsigned int lineno = 1;
    unsigned int linepos = 1;
    unsigned int position = 0;

    std::string * source;
    std::string current_word;
} Reader;

#endif