use crate::core::Token;
use crate::core::TokenType;

use std::io::Write;

macro_rules! logfile { () => { "debug.log" }; }

pub fn tokens(tokens: &Vec<Token>)
{
    match std::fs::OpenOptions::new().create(true).append(true).open(logfile!())
    {
        Ok(mut file) =>
        {
            match writeln!(file, "===== [ DEBUG :: TOKENS ] =====\n") { Ok(_) => {}, _ => panic!("Can't write file"), }
            for (token_type, token) in tokens.iter()
            {
                let t: &str = match token_type
                {
                    TokenType::STRING       => "TXT",
                    TokenType::NUMBER       => "NUM",
                    TokenType::LITERAL      => "LIT",
                    TokenType::DELIMITER    => "DLM",
                };
                match writeln!(file, "\t\t{}     {}", t, token) { Ok(_) => {}, _ => panic!("Can't write file"), }
            }
            match writeln!(file, "\n===============================\n") { Ok(_) => {}, _ => panic!("Can't write file"), }
        }
        _ => panic!("Can't open or create the file"),
    }
}