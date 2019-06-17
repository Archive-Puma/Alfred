mod arguments;
mod lexer;

fn main() {
    let args: arguments::Arguments = arguments::get_arguments();
    let source: String = match std::fs::read_to_string(&args.file)
    {
        Ok(src) => src,
        _       => String::new()
    };
    let tokens: Vec<lexer::Token> = lexer::tokenize(&source);
    println!("{:?}", tokens);
}
