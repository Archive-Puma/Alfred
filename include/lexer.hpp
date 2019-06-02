#ifndef LEXER_HPP
#define LEXER_HPP 1

#include <vector>
#include <string>
#include <cstdint>
#include <utility>

#include "error.hpp"
#include "utils.hpp"
#include "reader.hpp"

typedef struct {
    bool word = false;
    bool alfred = false;
    bool string = false;
    bool comment = false;
    bool escaped = false;
} Flags;

enum TokenType { LITERAL, STRING, NUMBER, OP, BINOP, DELIM, UNKNOWN };
typedef std::pair<TokenType,std::string> Token;
typedef std::vector<Token> Tokens;

Tokens lex(std::string * source);

void process(unsigned char c);

void dot(void);
void comma(void);
void string(void);
void comment(void);
void newline(void);
void whitespace(void);
void symbol(TokenType t, unsigned char c);

void new_word(void);
void new_token(TokenType type);
void append_word(unsigned char c);

void check_alfred(std::string word);

#endif