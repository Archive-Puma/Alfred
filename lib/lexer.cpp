#include "lexer.hpp"

Flags flags;
Reader reader;

#include <iostream>

void lex(std::string source)
{
    while(reader.position < source.length())
    {
        process(source[reader.position]);

        reader.position++;
    }
    process(' ');

    std::cout << reader.lineno << "," << reader.linepos << std::endl;
}

void process(unsigned char c)
{
    reader.linepos++;
    if(flags.comment)
    {
        if(c == ')') flags.comment = false;
        else return;
    } else switch(c)
    {
        case '(': flags.comment = true; break;
        case '"': flags.string = !flags.string; break;
        case '\n': newline(); break;
        case ' ':
        case '.':
        case ',': whitespace(); break;
        default: append_word(c); break;
    }
}

// -----------------------------------------------------------------

void newline(void)
{    
    reader.lineno++;
    reader.linepos = 1;

    whitespace();
}

void whitespace(void)
{
    if(flags.string) append_word(' ');
    else if(flags.word)
    {
        flags.word = false;
        if(!flags.alfred) check_alfred(reader.current_word);
        std::cout << reader.current_word << std::endl;
        reader.current_word = "";
    }
}

void append_word(unsigned char c)
{
    flags.word = true;
    reader.current_word.push_back(c);
}

// -----------------------------------------------------------------

void check_alfred(std::string word)
{
    if(tolower(word).compare("alfred") == 0) flags.alfred = true;
    else alfred_error(reader.lineno, reader.linepos - word.length() - 1, word);
}