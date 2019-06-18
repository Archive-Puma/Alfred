use std::io::Read;

pub fn get_source(path: &std::path::PathBuf) -> String
{
    let mut source: String;
    let file = std::fs::File::open(path);
    match file
    {
        Ok(mut buffer) => {
            let mut bytes = Vec::<u8>::new();
            if buffer.read_to_end(&mut bytes).is_err() { panic!("Jmmm"); }
            
            let mut index: usize = bytes.len() - 1;
            while index > 0 && bytes[index] != 0x00 { index -= 1; }
            let (_,bytes_src): (_,&[u8]) = bytes.split_at(index+1);
            source = String::from_utf8(bytes_src.to_vec()).unwrap_or_default();
        }
        _ => panic!("Some error in the binary"),
    }
    return source;
}