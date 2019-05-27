#include "io.hpp"

std::string readFile(std::string filename)
{
    // Read from file
    std::string source;
    std::stringstream buffer;
    std::ifstream input(filename);  // Open the file

    if(input.fail())                // Check if file exists
        file_error(filename);
    buffer << input.rdbuf();        // Save contents in a buffer
    source = buffer.str();          // Get the string from he buffer
    input.close();                  // Close the file

    return source;
}

void writeLexLog(Tokens tokens)
{
    std::string filename = "alfred-lex.log";
    std::ofstream output(filename);

    if(output.fail())                           // Check if we can create/access to the file
        file_error(filename);
    output.clear();
    output << "Type -- Value" << std::endl;
    output << "=============" << std::endl;
    for(Token t : tokens)
        output << "  " << t.first << "  --  "<< t.second << std::endl;
    output.close();
}

void writeParseLog(AST ast)
{
    std::string filename = "alfred-parser.log";
    std::ofstream output(filename);

    if(output.fail())                           // Check if we can create/access to the file
        file_error(filename);
    output.clear();
    output << "     Abstract Syntax Tree" << std::endl;
    output << "=====================================" << std::endl;
    output << "[ ";
    for(Node * n : ast)
        output << n->toString() << " ";
    output << "]" << std::endl;
    output.close();
}