#include "io.hpp"
#include "lexer.hpp"
#include "parser.hpp"
#include "arguments.hpp"

int main(int argc, char* argv[])
{
    Arguments args;
    std::string source;
    
    std::string zippedsrc = readSelf(argv[0]);
    if(zippedsrc.empty())
    {
        args = parseArguments(argc,argv);

        if(args.help) show_help(std::string(argv[0]));      // Show the help message
        else if(args.version) ; // show_version(version);
        else if(args.interactive) ; // repl();
        else if(!args.filename.empty())
            source = readFile(args.filename);
    } else source = zippedsrc;

    if(!source.empty())
    {           
        Tokens tokens = lex(&source);                   // Tokenize the source code
        if(args.debug) writeLexLog(tokens);
        
        AST ast = parse(tokens);                  // Generate the AST

        if(args.debug) writeParseLog(ast);

        for(Node * node : ast)                          // Evaluate the AST
            node->evaluate();
    }

    return 0;
}