pub struct Arguments
{
    pub repl:   bool,
    pub debug:  bool,
    pub file:   std::path::PathBuf,
}
impl Arguments {
    fn new() -> Arguments
    {
        Arguments {
            file: std::path::PathBuf::new(), repl: false, debug: false }
    }
}

fn display_help(name: &str)
{
    println!("Sólamente otro lenguaje de programación...

USO:
    {} [OPCIONES] [ARCHIVO]

OPCIONES:
    -d              Genera archivos de depuración
    -i              Corre el modo interactivo (REPL)"
    , name);

    std::process::exit(1);
}

pub fn get_arguments() -> Arguments
{
    let mut args: Arguments = Arguments::new();

    let argv: Vec<String> = std::env::args().collect();

    let program_name: &str = "alfred";
    let arg0_abs: std::path::PathBuf = std::path::PathBuf::from(&argv[0]);
    let arg0: &str = match arg0_abs.file_name()
    {
        None => program_name,
        Some(raw_name) => match raw_name.to_str()
        {
            Some(name) => name,
            _ => program_name,
        }
    };
    
    if argv.len() == 1 { display_help(arg0); }
    let mut index: usize = 1;
    while index < argv.len()
    {
        let cmd = &argv[index];
        match &cmd[..]
        {
            "-d" | "--debug" => args.debug = true,
            "-i" | "--interactive" => args.repl = true,
            _ => {
                let path: std::path::PathBuf = std::path::PathBuf::from(&cmd);
                if path.exists() && path.is_file() { args.file = path; }
                else { display_help(arg0); }
            }
        }
        index += 1;
    }

    return args;
}