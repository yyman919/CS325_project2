import sys
from bs4 import BeautifulSoup
import os

def extract_comments(input_file, output_dir):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            text = infile.read()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(text, 'html.parser')

        # Define a custom filter function to select only <p> tags without class attributes
        def is_valid_paragraph(tag):
            return tag.name == 'p' and not tag.has_attr('class')

        # Find all valid <p> tags and extract their text
        paragraphs = soup.find_all(is_valid_paragraph)
        comments = []

        for paragraph in paragraphs:
            # Extract the text within the <p> tags
            comment_text = paragraph.get_text().strip()

            # Only add non-empty comments
            if comment_text:
                comments.append(comment_text)

        if not comments:
            print("No comments found in the input file.")
        else:
            count = 1
            while True:
                output_file = os.path.join(output_dir, f'comments{count}.txt')
                if not os.path.exists(output_file):
                    break
                count += 1

            with open(output_file, 'w', encoding='utf-8') as outfile:
                for comment in comments:
                    outfile.write(comment + '\n\n')

            print(f"Comments extracted and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 extract_comments.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = '.'  # Output directory is the current directory

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    extract_comments(input_file, output_dir)

if __name__ == '__main__':
    main()
