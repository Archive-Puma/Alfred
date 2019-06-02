#include "lexer.hpp"

Flags flags;
Reader reader;
Tokens tokens;

Tokens lex(std::string * source)
{
    reader.source = source;
    while(reader.position < source->length())
    {
        process(source->at(reader.position));
        reader.position++;
    }
    if(!reader.current_word.empty()) new_word();
    
    return tokens;
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
    } else {
        switch(c)
        {
            case '(': comment(); break;  // Iniciamos un comentario
            case '"': string(); break;              // Iniciamos/cerramos una cadena de texto
            case '\n': newline(); break;            // Procesamos una nueva línea
            case ',': comma(); break;               // Parseamos comas según sean separadores o puntos decimales
            case '.': dot(); break;                 // Parseamos puntos según sean separadores o concatenadores
            case '\t': 
            case ' ': whitespace(); break;          // Parseamos los espacios
            case '[':
            case ']':
            case '{':
            case '}':
            case '!': symbol(OP,c); break;
            case '<':
            case '>':
            case '=':
            case '&':
            case '|':
            case '+':
            case '-':
            case '/':
            case '*':
            case '^':
            case '%': symbol(BINOP,c); break;             // Parseamos los símbolos
            default: append_word(c); break;         // Añadimos la letra a una palabra
        }
        flags.escaped = false;                      // Eliminamos secuencias de escape huérfanas
    }
}

// -----------------------------------------------------------------

void comma(void)
{
    if(flags.string) append_word(','); // Si es parte de un texto, añadimos la coma
    else
    {
        if(flags.word) new_word(); // Si estábamos parseando una palabra, la añadimos
        // Parseamos el delimitador
        reader.current_word = ",";
        new_token(DELIM);
    }
}

void dot(void)
{
    if(flags.string) append_word('.'); // Si es un texto, lo agregamos
    else
    {
        if(flags.word)
        {
            if(reader.position+1 < reader.source->size())
            {
                unsigned char next = reader.source->at(reader.position+1);
                if(util::isnum(reader.current_word))
                {
                    if(next < '0' || next > '9')
                    {
                        new_word();
                        reader.current_word = ".";
                        new_token(DELIM);
                    } else append_word('.');
                } else {
                    new_word();
                    reader.current_word = ".";
                    new_token(DELIM);
                }
            } else
            {
                new_word();
                reader.current_word = ".";
                new_token(DELIM);
            }
        } else
        {
            if(reader.position+1 < reader.source->size())
            {
                unsigned char next = reader.source->at(reader.position+1);
                if(next == '.')
                {
                    reader.current_word = "..";
                    new_token(OP);
                    reader.linepos++;
                    reader.position++;
                } else {
                    reader.current_word = ".";
                    new_token(DELIM);
                }
            } else
            {
                reader.current_word = ".";
                new_token(DELIM);
            }
        }
    }
}

void string(void)
{
    if(flags.escaped)                       // Comprobamos secuencias de escape
    {
        flags.escaped = false;
        if(flags.string) append_word('"');  // Añadimos el caracter escapado
    } else if(flags.string) {
        flags.string = false;
        new_token(STRING);
    } else flags.string = true; 
}

void comment(void)
{
    if(flags.string) append_word('(');
    else flags.comment = true;
}

void newline(void)
{    
    reader.lineno++;
    reader.linepos = 1;

    if(flags.string) append_word('\n');
    else if(flags.word) new_word();
}

void whitespace(void)
{
    if(flags.string) append_word(' ');
    else if(flags.word) new_word();
}

void symbol(TokenType t, unsigned char c)
{
    if(flags.string) append_word(c);
    else
    {
        if(flags.word) new_word();
        reader.current_word = c;
        new_token(t);
    }
}

void new_word(void)
{
    if(!flags.alfred) check_alfred(reader.current_word);
    else {            
        if(util::iscnum(reader.current_word))
            new_token(NUMBER);
        else if(util::tolower(reader.current_word).compare("y") == 0)
            new_token(DELIM);
        else new_token(LITERAL);
    }
}

void new_token(TokenType type)
{
    flags.word = false;
    tokens.push_back(Token(type,reader.current_word));
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
    if(util::tolower(word).compare("alfred") == 0)
    {
        flags.word = false;
        flags.alfred = true;
        reader.current_word.clear();
    }
    else alfred_error(reader.lineno, reader.linepos - word.length() - 1, word);
}