from fpdf import FPDF
import string

# Function to read data from a file and analyze it
def analyze_file(file_path):
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Initialize variables for analysis
        total_lines = len(lines)
        total_words = 0
        unique_words = set()
        word_count = {}
        
        # Analyze the data line by line
        for line in lines:
            # Remove punctuation and convert to lowercase for consistent word counting
            line = line.translate(str.maketrans("", "", string.punctuation)).lower()
            words = line.split()
            total_words += len(words)
            
            # Update word counts and unique words
            for word in words:
                unique_words.add(word)
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        
        # Calculate some basic statistics
        avg_words_per_line = total_words / total_lines if total_lines > 0 else 0
        most_frequent_word = max(word_count, key=word_count.get) if word_count else None
        most_frequent_count = word_count.get(most_frequent_word, 0)

        return {
            'total_lines': total_lines,
            'total_words': total_words,
            'unique_words': len(unique_words),
            'avg_words_per_line': avg_words_per_line,
            'most_frequent_word': most_frequent_word,
            'most_frequent_count': most_frequent_count,
            'word_count': word_count
        }
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Function to generate a PDF report using the analysis data
def generate_pdf_report(report_data,output_pdf_path):
    # Create PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Set title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'File Analysis Report', ln=True, align='C')
    pdf.ln(10)  # Add some space
    
    # Set font for body text
    pdf.set_font('Arial', '', 12)

    # Write the analysis data to the PDF
    pdf.cell(200, 10, f"Total Lines: {report_data['total_lines']}", ln=True)
    pdf.cell(200, 10, f"Total Words: {report_data['total_words']}", ln=True)
    pdf.cell(200, 10, f"Unique Words: {report_data['unique_words']}", ln=True)
    pdf.cell(200, 10, f"Average Words per Line: {report_data['avg_words_per_line']:.2f}", ln=True)
    pdf.cell(200, 10, f"Most Frequent Word: '{report_data['most_frequent_word']}' (Appears {report_data['most_frequent_count']} times)", ln=True)
    
    pdf.ln(10)  # Add some space
    pdf.cell(200, 10, 'Word Frequency:', ln=True)
    
    # Display word frequencies
    for word, count in report_data['word_count'].items():
        pdf.cell(200, 10, f"{word}: {count}", ln=True)

    # Save the PDF to the specified file
    pdf.output(output_pdf_path)
    print(f"PDF report generated: {output_pdf_path}")


# Main function to read file, analyze data, and generate PDF report
def main(file_path,output_pdf_path):
    # Analyze the file
    analysis_data = analyze_file(file_path)
    
    if analysis_data:
        # Generate the PDF report
        generate_pdf_report(analysis_data, output_pdf_path)


# Example usage
file_path = "C:\\Users\\navee\\Documents\\exa.txt"  # Replace with your file path
output_pdf_path = "C:\\Users\\navee\\OneDrive\\Desktop\\analysis_report.pdf" # Replace with a valid path
main(file_path,output_pdf_path)
