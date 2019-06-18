pub struct Arguments
{
    pub repl:       bool,
    pub name:       String,
    pub file:       std::path::PathBuf,
    pub path:       std::path::PathBuf,
    pub debug:      bool,
    pub itself:     bool,
}
impl Arguments {
    fn new() -> Arguments
    {
        Arguments {
            name: String::new(),
            file: std::path::PathBuf::new(),
            path: std::path::PathBuf::new(),
            itself: false, repl: false, debug: false,
            }
    }
}

pub fn display_help(name: &str)
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

    let default_name: String = String::from("alfred");
    args.path = std::path::PathBuf::from(&argv[0]);
    args.name = match &args.path.file_name()
    {
        None => default_name,
        Some(raw_name) => match raw_name.to_str()
        {
            Some(name) => name.to_string(),
            _ => default_name,
        }
    };
    
    if argv.len() == 1 { args.itself = true; }
    else {
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
                    else { display_help(&args.name); }
                }
            }
            index += 1;
        }
    }

    return args;
}