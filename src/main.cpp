// * Imports

#include "io.hpp"
#include "lexer.hpp"
#include "parser.hpp"
#include "arguments.hpp"

/**
 * Entrypoint of the program
 * 
 * - Check executable contains source code
 * - Parse arguments
 * - Source => Lexer -> Parser -> Evaluator
 * 
 * @param argc Number of arguments
 * @param argv CLI arguments
 * @return Exit code
 */
int main(int argc, char* argv[])
{
    Arguments args;
    std::string source;
    
    // ? Check if the executable contains code
    std::string zippedsrc = readSelf(argv[0]);
    // ? False : Parse args and get source code from file
    if(zippedsrc.empty())
    {
        args = parseArguments(argc,argv);

        if(args.help) show_help(std::string(argv[0]));  // Show the help message
        else if(args.version) ; // TODO: show_version(version);
        else if(args.interactive) ; // TODO: repl();    // Run REPL
        else if(!args.filename.empty())                 // Get the source code from file
            source = readFile(args.filename);
    // ? True : Get the soruce code from itself
    } else source = zippedsrc;

    // ? Check if source code exists
    // ? True: Source => Lexer -> Parser -> Evaluator
    if(!source.empty())
    {
        // Tokenize the source code
        Tokens tokens = lex(&source);
        if(args.debug) writeLexLog(tokens);
        // Generate the AST
        AST ast = parse(tokens);
        if(args.debug) writeParseLog(ast);
        // Evaluate the AST
        for(Node * node : ast)
            node->evaluate();
    }

    // Exit code
    return 0;
}