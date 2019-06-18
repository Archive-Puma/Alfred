mod lib;
use lib::*;

fn main() {
    let mut source: String;
    let args: env::Arguments = env::get_arguments();

    if args.itself { source = utils::get_source(&args.path); }
    else { source = std::fs::read_to_string(&args.file).unwrap_or_default(); }

    if !source.is_empty()
    {
        let tokens: Vec<core::Token> = core::tokenize(&source);
        if args.debug { log::tokens(&tokens); }
    }
    else { env::display_help(&args.name); }
}
