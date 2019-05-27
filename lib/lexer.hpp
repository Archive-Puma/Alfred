#ifndef LEXER_HPP
#define LEXER_HPP 1

#include <vector>
#include <string>
#include <cstdint>

#include "error.hpp"
#include "utils.hpp"

typedef struct {
    bool word = false;
    bool alfred = false;
    bool string = false;
    bool comment = false;

    unsigned int depth = 0;
} Flags;

typedef struct {
    unsigned int lineno = 1;
    unsigned int linepos = 1;
    unsigned int position = 0;

    std::string current_word;
} Reader;

void lex(std::string source);
void process(unsigned char c);

void newline(void);
void whitespace(void);
void append_word(unsigned char c);

void check_alfred(std::string word);

#endif