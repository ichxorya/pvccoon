/* Import the required libraries. */
use std::fs; // For reading files.
use polars::prelude::*; // For the DataFrame struct.

/* Define the Lexer methods. */

/// Load files: Load the transition table and the .vc file.
pub fn load_files(vc_path: &str) -> (DataFrame, Vec<char>) {
    // Load the transition table.
    let transition_table: DataFrame = CsvReader::from_path("src/lexer/transition_table.dat").unwrap().finish().unwrap();

    // Load the .vc file and do left/right-filtering.
    let vc_file: String = fs::read_to_string(vc_path).expect("Unable to read the .vc file.");
    let vc_file: String = vc_file.trim_start().to_string();
    let vc_file: String = vc_file.trim_end().to_string();

    // Convert the .vc file to a vector of characters.
    let vc_file: Vec<char> = vc_file.chars().collect::<Vec<char>>();

    // Return the transition table and the .vc file.
    (transition_table, vc_file)
}
