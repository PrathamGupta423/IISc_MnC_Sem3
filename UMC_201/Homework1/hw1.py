# NOTHINg in this file should be modified

from count_pairs import count_pairs_file
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Run {sys.argv[0]} with arguments <filename>')
        sys.exit(1)
    # Open the file argv[1]
    filename = sys.argv[1]
    # Call count_pairs_file and print the result
    print(count_pairs_file(filename))