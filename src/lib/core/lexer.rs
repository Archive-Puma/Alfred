#[derive(PartialEq)]
enum State
{
    RAW, COMMENT,
    LITERAL, STRING, ESCAPED, NUMBER, DECIMAL
}

#[derive(Debug)]
pub enum TokenType { LITERAL, STRING, NUMBER, DELIMITER }
pub type Token = (TokenType, String);

pub fn tokenize(source: &str) -> Vec<Token>
{
    let mut tokens: Vec<Token> = Vec::new();

    let mut state: State = State::RAW;
    let mut current_str: String = String::new();

    for (index, ch) in source.chars().enumerate()
    {        
        if state == State::RAW
        {
            match ch
            {
                '"' => state = State::STRING,
                '(' => state = State::COMMENT,
                '0' ... '9' => { current_str.push(ch); state = State::NUMBER; }
                'a' ... 'z' | 'A' ... 'Z' => { current_str.push(ch); state = State::LITERAL; }
                ' ' | '\n' | '\t' | '\r' => continue,
                '.' | ',' => tokens.push((TokenType::DELIMITER, ch.to_string())),
                _ => panic!("Unexpected token in RAW state: {}", ch),
            }
        }
        else if state == State::COMMENT
        {
            if ch == ')' { state = State::RAW; }
        }
        else if state == State::STRING
        {
            match ch
            {
                '\\' => state = State::ESCAPED,
                '"' => {
                    tokens.push((TokenType::STRING, current_str.clone()));
                    current_str.clear();
                    state = State::RAW;
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
                _ => panic!("Unexpected token in ESCAPED state: {}", ch),
            }
            state = State::STRING;
        }
        else if state == State::NUMBER
        {
            match ch
            {
                '0' ... '9' => current_str.push(ch),
                '.' => {
                    match source.chars().nth(index+1)
                    {
                        Some(character) => match character
                        {
                            '0' ... '9' => {
                                current_str.push(ch);
                                state = State::DECIMAL;
                            }
                            _ => {
                                tokens.push((TokenType::NUMBER, current_str.clone()));
                                tokens.push((TokenType::DELIMITER, ch.to_string()));
                                current_str.clear();
                                state = State::RAW;
                            }
                        }
                        None => {
                            tokens.push((TokenType::NUMBER, current_str.clone()));
                            tokens.push((TokenType::DELIMITER, ch.to_string()));
                            current_str.clear();
                            state = State::RAW;
                        }
                    }
                }
                ',' => {
                    tokens.push((TokenType::NUMBER, current_str.clone()));
                    tokens.push((TokenType::DELIMITER, ch.to_string()));
                    current_str.clear();
                    state = State::RAW;
                }
                ' ' | '\n' | '\t' | '\r' => {
                    tokens.push((TokenType::NUMBER, current_str.clone()));
                    current_str.clear();
                    state = State::RAW;
                }
                _ => panic!("Unexpected token in NUMBER state: {}", ch),
            }
        }
        else if state == State::DECIMAL
        {
            match ch
            {
                '0' ... '9' => current_str.push(ch),
                '.' | ',' => {
                    tokens.push((TokenType::NUMBER, current_str.clone()));
                    tokens.push((TokenType::DELIMITER, ch.to_string()));
                    current_str.clear();
                    state = State::RAW;
                }
                ' ' | '\n' | '\t' | '\r' => {
                    tokens.push((TokenType::NUMBER, current_str.clone()));
                    current_str.clear();
                    state = State::RAW;
                }
                _ => panic!("Unexpected token in NUMBER state: {}", ch),
            }
        }
        else if state == State::LITERAL
        {
            match ch
            {
                '0' ... '9' | 'a' ... 'z' | 'A' ... 'Z' => current_str.push(ch),
                ' ' | '\n' | '\t' | '\r' => {
                    tokens.push((TokenType::LITERAL, current_str.clone()));
                    current_str.clear();
                    state = State::RAW;
                }
                '.' | ',' => {
                    tokens.push((TokenType::LITERAL, current_str.clone()));
                    tokens.push((TokenType::DELIMITER, ch.to_string()));
                    current_str.clear();
                    state = State::RAW;
                }
                _ => panic!("Unexpected token in LITERAL state: {}", ch),
            }
        }
    }
    if state != State::RAW { panic!("Syntax error. Should end in a RAW state"); }
    return tokens;
}