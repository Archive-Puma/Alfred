#include "io.hpp"
#include "lexer.hpp"
#include "parser.hpp"
#include "arguments.hpp"

int main(int argc, char* argv[])
{
    Arguments args = parseArguments(argc,argv);
    if(args.help) show_help(std::string(argv[0]));
    else if(args.version) ; // show_version(version);
    else if(args.interactive) ; // repl();
    else if(!args.filename.empty())
    {
        std::string source = readFile(args.filename);   // Read the source code
        
        Tokens tokens = lex(&source);                   // Tokenize the source code
        if(args.debug) writeLexLog(tokens);
        
        AST ast = generateAST(tokens);                  // Generate the AST
        if(args.debug) writeParseLog(ast);

        for(Node * node : ast)                          // Evaluate the AST
            node->evaluate();
    }

    return 0;
}