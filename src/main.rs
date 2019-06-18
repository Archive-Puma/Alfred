mod lexer;
mod arguments;
mod self_reader;

fn main() {
    let mut source: String = String::new();
    let args: arguments::Arguments = arguments::get_arguments();

    if args.itself
    {
        source = self_reader::get_source(&args.path);
    }
    else
    {
        let content = std::fs::read_to_string(&args.file);
        if content.is_ok() { source = content.unwrap(); }
    }
    

    if !source.is_empty()
    {
        let tokens: Vec<lexer::Token> = lexer::tokenize(&source);
        println!("{:?}", tokens);
    }
    else { arguments::display_help(&args.name); }
}
