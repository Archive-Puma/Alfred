#[derive(Debug)]
pub enum TokenType
{
    KEYWORD, ARGUMENT, STRING, NUMBER, DELIMITER
}

#[derive(Clone,PartialEq)]
enum State
{
    NONE, COMMENT,
    KEYWORD, ARGUMENTS,
    STRING, ESCAPED, NUMBER, DECIMAL
}

pub type Token = (TokenType, String);
pub fn tokenize(source: &str) -> Vec<Token>
{
    let keywords: Vec<&str> = vec![
        "escribe", "di"
    ];

    let mut tokens: Vec<Token> = Vec::new();

    let mut state: State = State::NONE;
    let mut current_str: String = String::new();
    let mut previous_state: State = State::NONE;

    for (index, ch) in source.chars().enumerate()
    {        
        if state == State::NONE
        {
            match ch
            {
                ' ' | '\n' | '\t' | '\r' => continue,
                '(' => {
                    previous_state = state;
                    state = State::COMMENT;
                }
                'a' ... 'z' | 'A' ... 'Z' => {
                    current_str.push(ch);
                    state = State::KEYWORD;
                }
                _ => panic!("Unexpected token"),
            }
        }
        else if state == State::COMMENT
        {
            if ch == ')' { state = previous_state.clone(); }
        }
        else if state == State::KEYWORD
        {
            match ch
            {
                ' ' => current_str.push(ch),
                'a' ... 'z' | 'A' ... 'Z' | '0' ... '9' => {
                    current_str.push(ch);
                    let current_tolower: String = current_str.to_lowercase();
                    if keywords.contains(&current_tolower.as_ref())
                    {
                        tokens.push((TokenType::KEYWORD, current_tolower));
                        current_str.clear();
                        state = State::ARGUMENTS;
                    }
                }
                _ => panic!("Keyword not found (Maybe function or variable assigment"),
            }
        }
        else if state == State::ARGUMENTS
        {
            match ch
            {
                '(' => {
                    previous_state = state;
                    state = State::COMMENT;
                }
                '"' => {
                    if !current_str.trim().is_empty()
                    {
                        let current_tolower: String = current_str.trim().to_lowercase();
                        tokens.push((TokenType::ARGUMENT, current_tolower));
                    }
                    current_str.clear();
                    state = State::STRING;
                }
                '0' ... '9' => {
                    if !current_str.trim().is_empty()
                    {
                        let current_tolower: String = current_str.trim().to_lowercase();
                        tokens.push((TokenType::ARGUMENT, current_tolower));
                    }
                    current_str.clear();
                    current_str.push(ch);
                    state = State::NUMBER;
                }
                ' ' | '\n' | '\t' | '\r' => {
                    if !current_str.ends_with(' ') { current_str.push(' '); }
                }
                'a' ... 'z' | 'A' ... 'Z' => current_str.push(ch),
                '.' => {
                    if !current_str.trim().is_empty()
                    {
                        let current_tolower: String = current_str.trim().to_lowercase();
                        tokens.push((TokenType::ARGUMENT, current_tolower));
                    }
                    current_str.clear();
                    tokens.push((TokenType::DELIMITER, ch.to_string()));
                    state = State::NONE
                }
                _ => panic!("Unknown token: {}", ch),
            }
        }
        else if state == State::STRING
        {
            match ch
            {
                '\\' => state = State::ESCAPED,
                '"' => {
                    tokens.push((TokenType::STRING, current_str.clone()));
                    current_str.clear();
                    state = State::ARGUMENTS;
                }
                _ => current_str.push(ch),
            }
        }
        else if state == State::ESCAPED
        {
            match ch
            {
                '"' => current_str.push('\"'),
                'n' => current_str.push('\n'),
                'r' => current_str.push('\r'),
                't' => current_str.push('\t'),
                '0' => current_str.push('\0'),
                '\\' => current_str.push('\\'),
                '\'' => current_str.push('\''),
                _ => panic!("Unknown character escape: {}", ch),
            }
            state = State::STRING;
        }
        else if state == State::NUMBER
        {
            match ch
            {
                '.' => {
                    match source.chars().nth(index+1)
                    {
                        Some(c) => match c
                        {
                            '0' ... '9' => {
                                current_str.push(ch);
                                state = State::DECIMAL;
                            }
                            _ => {
                                tokens.push((TokenType::NUMBER, current_str.clone()));
                                tokens.push((TokenType::DELIMITER, ch.to_string()));
                                current_str.clear();
                                state = State::NONE;
                            }
                        }
                        None => {
                            tokens.push((TokenType::NUMBER, current_str.clone()));
                            tokens.push((TokenType::DELIMITER, ch.to_string()));
                            current_str.clear();
                            state = State::NONE;
                        }
                    }
                }
                '0' ... '9' => current_str.push(ch),
                _ => {
                    tokens.push((TokenType::NUMBER, current_str.clone()));
                    current_str.clear();
                    current_str.push(ch);
                    state = State::ARGUMENTS;
                }
            }
        }
        else if state == State::DECIMAL
        {
            match ch
            {
                '0' ... '9' => current_str.push(ch),
                '.' => {
                    tokens.push((TokenType::NUMBER, current_str.clone()));
                    tokens.push((TokenType::DELIMITER, ch.to_string()));
                    current_str.clear();
                    state = State::NONE;
                }
                _ => {
                    tokens.push((TokenType::NUMBER, current_str.clone()));
                    current_str.clear();
                    current_str.push(ch);
                    state = State::ARGUMENTS;
                }
            }
        }
    }
    if state != State::NONE { panic!("Syntax error"); }
    return tokens;
}