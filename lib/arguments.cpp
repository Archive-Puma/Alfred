#include "arguments.hpp"

Arguments parseArguments(int argc, char* argv[])
{
    int option;
    Arguments args;

    if(argc == 1) args.help = true;
    else while((option = getopt(argc,argv,"f:hiv")) != EOF)
    {
        switch(option)
        {
            case 'f': args.filename = optarg;   break;
            case 'i': args.interactive = true;  break;
            case 'h': args.help = true;         break;
            case 'v': args.version = true;      break;
            default: args.help = true;          break;
        }
    }

    return args;
}

void show_help(std::string program)
{
    std::string help =
R"(Uso: )" + program + R"( [-i|-f archivo.alf] [-h] [-v]
    
Opciones de ejecución:
  -f ARCHIVO      Ejecuta el programa leyendo un archivo.
  -i              Ejecuta el programa de forma interactiva (REPL).
Opciones estándar:
  -h              Muestra esta ayuda y sale.
  -v              Muestra la versión y sale.)";

    std::cout << help << std::endl;
}

