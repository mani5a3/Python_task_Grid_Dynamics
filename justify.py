import argparse
from justify_paragraph.paragraph_formatter import justify_paragraph

def main():
    parser = argparse.ArgumentParser(description='Justify Paragraph')
    parser.add_argument('--paragraph-string', type=str, help='Input paragraph string')
    parser.add_argument('--paragraph-width', type=int, help='Width of each line in the paragraph')
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f"Error parsing arguments: {e}")
    
    if not args.paragraph_string or not args.paragraph_width:
        print("Please provide both --paragraph-string and --paragraph-width arguments.")
        return

    justified_array = justify_paragraph(args.paragraph_string, args.paragraph_width)

    for i, line in enumerate(justified_array, 1):
        print(f"Array [{i}] = \"{line}\"")

if __name__ == "__main__":
    main()
