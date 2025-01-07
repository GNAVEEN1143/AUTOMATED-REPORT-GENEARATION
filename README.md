# AUTOMATED-REPORT-GENEARATION

Name: GADAPA NAVEEN KUMAR

Company: CODTECH IT SOLUTIONS

ID: CT0806AW

Domain: Python Programming

Duration: December 2024 to January 2025

Mentor: N.Santosh

Project: AUTOMATED-REPORT-GENEARATION

Overview:

The provided Python program performs text file analysis and generates a PDF report summarizing the analysis. Here's an overview of how the code is structured:

### Key Components:

1. **`analyze_file(file_path)`**:
   - **Purpose**: Reads the content of a text file, performs analysis on it, and returns key statistics about the file's content.
   - **Steps**:
     - **Reads the file**: Opens and reads the content of the file at `file_path`.
     - **Text processing**:
       - Removes punctuation from each line using `str.maketrans()`.
       - Converts the text to lowercase to ensure case-insensitivity in word counting.
     - **Metrics**:
       - Calculates the total number of lines in the file.
       - Counts total words and keeps track of unique words using a set.
       - Tracks the frequency of each word using a dictionary (`word_count`).
     - **Basic statistics**:
       - Calculates the average number of words per line.
       - Identifies the most frequent word and how many times it appears.
   - **Returns**: A dictionary with statistics like the number of lines, total words, unique words, average words per line, the most frequent word, and its frequency.

2. **`generate_pdf_report(report_data, output_pdf_path)`**:
   - **Purpose**: Generates a PDF report based on the analysis data provided by `analyze_file()`.
   - **Steps**:
     - Uses the `FPDF` library to create a PDF file.
     - Adds a title (`File Analysis Report`) and then appends details such as:
       - Total lines
       - Total words
       - Unique words
       - Average words per line
       - Most frequent word and its count
       - Word frequencies (every word in the file and how many times it appears).
   - **Saves the report**: The PDF is saved to the location specified in `output_pdf_path`.

3. **`main(file_path, output_pdf_path)`**:
   - **Purpose**: The main function that coordinates the entire process of analyzing the file and generating the PDF.
   - **Steps**:
     - Calls `analyze_file()` to perform the file analysis.
     - If analysis is successful, it calls `generate_pdf_report()` to generate the PDF report.
   
4. **Example Usage**:
   - The script uses an example file path (`file_path = "C:\\Users\\navee\\Documents\\exa.txt"`) to read a text file.
   - The report is saved as a PDF file to a specified location (`output_pdf_path = "C:\\Users\\navee\\OneDrive\\Desktop\\analysis_report.pdf"`).

### Steps in the Code:
1. **Text File Analysis**:
   - The function `analyze_file` reads a text file and calculates several statistics like the total number of lines, words, unique words, and the most frequent word.
   - It also computes the average number of words per line.

2. **Word Frequency Counting**:
   - The program maintains a dictionary of word counts and uses it to determine the most frequent word and its count. It also tracks the count of every word in the text file.

3. **PDF Report Generation**:
   - After the analysis, `generate_pdf_report` uses `FPDF` to create a PDF with detailed statistics on the file's content.
   - The PDF report includes the total number of lines, words, unique words, average words per line, and word frequency details.

4. **Error Handling**:
   - The function `analyze_file` includes basic error handling for file-related issues (e.g., file not found or other exceptions).
   - If an error occurs (e.g., the file is not found), the program prints an error message.

### Example Output of the PDF:
The PDF report will include:
   - **File Statistics**:
     - Total number of lines in the file.
     - Total number of words in the file.
     - Number of unique words.
     - Average words per line.
     - The most frequent word and how many times it appears.
   - **Word Frequency**: A list of all the words in the file along with their respective counts.

### Points to Consider:
- **File Path**: The paths (`file_path` and `output_pdf_path`) should be updated to match the correct file and destination on your system.
- **Text File**: The program assumes the file contains plain text. If the file format is different, additional handling may be needed.
- **Punctuation Removal**: The program removes all punctuation from the file for counting purposes. This means "word." and "word" are counted as the same word.
- **FPDF Library**: The `FPDF` library is used to generate the PDF. It provides a simple interface to create documents, but additional formatting (e.g., tables, page breaks) could be added for more complex reports.

### Final Thoughts:
This program is useful for text analysis tasks where you want to generate a PDF report with basic statistics (line count, word count, unique words, etc.) and detailed word frequency information. It's a good starting point for analyzing any text-based file and producing readable output in PDF format.

OUTPUT:

![Screenshot 2025-01-07 165157](https://github.com/user-attachments/assets/f4a3d833-e336-4532-a918-6e30c53433fa)
