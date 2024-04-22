import csv
import csv

def convert_csv_to_text(csv_file, text_file):
    """Converts a CSV file to a text file, preserving table structure."""

    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        with open(text_file, 'w', encoding='utf-8') as textfile:
            textfile.write(' | '.join(header) + '\n')
            for row in reader:
                formatted_row = ' | '.join(row)
                textfile.write(formatted_row + '\n')
if __name__ == '__main__':
    csv_file = input("Enter the CSV file path: ")
    text_file = input("Enter the text file path: ")
    convert_csv_to_text(csv_file, text_file)
    print(f"CSV file '{csv_file}' converted to text file '{text_file}'.")

