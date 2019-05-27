#include "lexer.hpp"

Flags flags;
Reader reader;
Tokens tokens;

#include <iostream>

void lex(std::string source)
{
    while(reader.position < source.length())
    {
        process(source[reader.position]);
        reader.position++;
    }
    whitespace();

    for(std::string token : tokens)
        std::cout << token << std::endl;
}

void process(unsigned char c)
{
    // Actualizamos la posición de la línea
    reader.linepos++;
    // Comprobamos si se intenta reaizar una secuncia de escape
    if(c == '\\' && !flags.escaped) flags.escaped = true;
    // Comprobamos si estamos dentro de un comentario
    else if(flags.comment)
    {
        if(flags.escaped) flags.escaped = false; // Ignoramos secuencias de escape en los comentarios
        else if(c == ')') flags.comment = false; // Comprobamos si nos hemos encontrado un fin de comentario
        else return; // Ignoramos los caracteres entre paréntesis
    } else if(flags.escaped && !flags.string) {
        // Comprobamos secuencias de escape fuera de textos y comentarios
        std::string token = "\\";
        token.push_back(c);
        token_error(reader.lineno, reader.linepos - 2, token);
    } else switch(c)
    {
        case '(': flags.comment = true; break;          // Iniciamos un comentario
        case '"': string(); break;                      // Iniciamos/cerramos una cadena de texto
        case '\n': newline(); break;                    // Procesamos una nueva línea
        case ' ':
        case '.':
        case ',': whitespace(); break;                  // Tratamos espacios, puntos y comas como espacios (de momento)
        default: append_word(c); break;                 // Añadimos la letra a una palabra
    }
}

// -----------------------------------------------------------------

void string(void)
{
    if(flags.escaped)
    {
        flags.escaped = false;
        if(flags.string) append_word('"');
    } else if(flags.string) {
        flags.string = false;
        new_token();
    } else flags.string = true; 
}

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
        if(!flags.alfred) check_alfred(reader.current_word);
        else new_token();
    }
}

void new_token(void)
{
    flags.word = false;
    tokens.push_back(reader.current_word);
    reader.current_word.clear();
}

void append_word(unsigned char c)
{
    flags.word = true;
    reader.current_word.push_back(c);
}

// -----------------------------------------------------------------

void check_alfred(std::string word)
{
    if(tolower(word).compare("alfred") == 0)
    {
        flags.word = false;
        flags.alfred = true;
        reader.current_word.clear();
    }
    else alfred_error(reader.lineno, reader.linepos - word.length() - 1, word);
}