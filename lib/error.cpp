#include "error.hpp"

void error(std::string type, std::string msg)
{
    std::cerr << "Error de " << type << ": " << msg << std::endl;
    exit(EXIT_FAILURE);
}

void file_error(std::string file)
{
    error("archivo", "No se ha podido abrir el archivo " + file + ".");
}

void alfred_error(unsigned int lineno, unsigned int linepos, std::string word)
{
    error("sintaxis (" + std::to_string(lineno) + "," + std::to_string(linepos) + ")",
        "Se esperaba la palabra clave 'Alfred' pero se ha hayado la palabra '" + word + "'.");
}