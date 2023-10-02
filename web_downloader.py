import urllib.request
import sys
import os.path
from urllib.parse import urlparse
import argparse

# Function to download the content of the URL
def download(url):
    try:
        # Open the URL and read its content
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        return text
    except urllib.error.URLError as e:
        print(f"Error: Unable to access the URL - {e.reason}")
        sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        sys.exit(1)

# Function to write the content of the URL into a text file
def write_file(url, text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Main function
def main():
    # Create an argument parser to accept the URL as a command-line argument
    parser = argparse.ArgumentParser(description='Download content from a URL and save it to a text file.')
    parser.add_argument('url', type=str, help='URL to download content from (include http:// or https://)')

    args = parser.parse_args()
    url = args.url

    # Check if the URL includes 'http://' or 'https://', and exit if not
    if not url.startswith('http://') and not url.startswith('https://'):
        print('Error: Invalid URL. Please include http:// or https://')
        sys.exit(1)

    # Download content from the URL
    text = download(url)

    # Generate a unique filename based on the number of existing "fileX.txt" files in the directory
    index = 1
    while True:
        filename = f'file{index}.txt'
        if not os.path.isfile(filename):
            break
        index += 1

    # Write the downloaded content to the generated filename
    write_file(url, text, filename)
    print(f"Content downloaded and saved to {filename}")

if __name__ == '__main__':
    main()
