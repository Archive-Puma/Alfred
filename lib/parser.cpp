#include "parser.hpp"

/**
 * @global current Current Node of the AST
 * @global processor All the flags and variables needed
*/
Node * current;
Processor processor;

/**
 * Parse the Tokens to get the Abstract Syntax Tree
 * 
 * @param tokens Tokenized source code
 * @return The AST generated
 */
AST parse(Tokens tokens)
{
    // Set the reserved keywords
    processor.reserved.reserve(RESERVLEN);
    processor.reserved = { "di" };
    // Initialize all the variables
    processor.init = false;
    processor.position = 0;
    processor.predict.clear();
    processor.tokens = &tokens;
    // ? Iterate over all the tokens
    while(processor.position < processor.tokens->size())
        get_next();
    // Return the AST generated
    return processor.ast;
}

/**
 * Parse the current token
 */
void get_next()
{
    // ? Check if the code begins with a delimiter (condition)
    if(!processor.init)
    {
        // ? False : Check the delimiter
        processor.init = currentType() == DELIM;
        if(!processor.init) ; // ! Error
    } else
    {
        // ? True : Check the token type
        switch(currentType())
        {
            // * LITERAL : Instruction | Variable
            case LITERAL:
                update_predict();   // Append actual value to the prediction
                if(make_predict())  // Check if there is a instruction with that name 
                    current = instruction(); // Get the instruction
                break;
            // * STRING : Value | LHS | RHS
            case STRING:
                if(current)
                {
                    // TODO: nextType() != TokenType::BINOP
                    current->append(new String(currentValue()));
                } else ; // ! Error
                break;
            // * NUMBER : Value | LHS | RHS
            case NUMBER:
                break;
            // * OP : { } ! [ ]
            case OP: break;
            // * BINOP : + - / * ^ % | & = > <
            case BINOP: break;
            // * DELIM : . ,
            case DELIM:
                // Append Node to AST
                if(current) processor.ast.emplace_back(current);
                // Clear Node and Prediction
                processor.predict.clear();
                current = nullptr;
                break;
            // * Other tokens (unsupported)
            default: break;
        }
    }
    // Update the processor position
    processor.position++;
}

/**
 * Append actual value to the prediction
 */
void update_predict()
{
    if(!processor.predict.empty())
        processor.predict += " ";
    processor.predict += util::tolower(currentValue());
}

/**
 * Check if the prediction is a reserved keyword
 * 
 * @return True if is a reserved keyword
 */
bool make_predict()
{
    bool end;
    std::vector<std::string> tmp;
    tmp.reserve(RESERVLEN);
    end = util::contains(processor.reserved, processor.predict);
    return end;
}

/**
 * Get the correspondent Node from a prediction
 * 
 * @return The correspondent Node
 */
Node * instruction()
{
    if(processor.predict.compare("di") == 0) return new Print();
    else return nullptr;
}

/**
 * Get the actual token type
 * 
 * @return The actual token type
 */
TokenType currentType()
{
    return processor.tokens->at(processor.position).first;
}

/**
 * Get the actual token value
 * 
 * @return The actual token value
 */
std::string currentValue()
{
    return processor.tokens->at(processor.position).second;
}

/**
 * Get the next token type
 * 
 * @return The next token type
 */
TokenType nextType()
{
    TokenType type = TokenType::UNKNOWN;
    if(processor.position + 1 < processor.tokens->size())
        type = processor.tokens->at(processor.position + 1).first;
    return type;
}

// https://mariusbancila.ro/blog/2009/02/05/evaluating-expressions-part-3-building-the-ast/