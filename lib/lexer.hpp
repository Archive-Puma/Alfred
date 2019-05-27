#ifndef LEXER_HPP
#define LEXER_HPP 1

#include <vector>
#include <string>
#include <cstdint>
#include <utility>

#include "error.hpp"
#include "utils.hpp"

typedef struct {
    bool word = false;
    bool alfred = false;
    bool string = false;
    bool comment = false;
    bool escaped = false;

    unsigned int depth = 0;
} Flags;

typedef struct {
    unsigned int lineno = 1;
    unsigned int linepos = 1;
    unsigned int position = 0;

    std::string * source;
    std::string current_word;
} Reader;

enum TokenType { LITERAL, STRING, NUMBER };
typedef std::pair<TokenType,std::string> Token;
typedef std::vector<Token> Tokens;

void lex(std::string * source);
void process(unsigned char c);

void comma(void);
void string(void);
void newline(void);
void whitespace(void);

void new_token(TokenType type);
void append_word(unsigned char c);

void check_alfred(std::string word);

#endif