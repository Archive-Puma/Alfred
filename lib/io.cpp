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