"""
Combines CSV files together
"""
import sys
import pandas as pd
from pathlib import Path


class CsvCombine:

    def __init__(self):
        """Initialize CSV file list"""
        if len(sys.argv) < 2:
            usage()
            exit(0)
        self.csvfiles = sys.argv[1:]


    def combine_csv(self):
        self.df_total = pd.DataFrame()
        for path_file in self.csvfiles:
            assert Path(path_file).is_file()

            dftemp = pd.read_csv(path_file, quotechar='"', escapechar="\\")
            dftemp['filename'] = Path(path_file).name

            print(self.df_total)
            self.df_total = pd.concat([self.df_total, dftemp])


    def print_combine(self):
        print(self.df_total)
        self.df_total.to_csv(sys.stdout, index=False)

    
    def combine_main(self):
        self.combine_csv()
        self.print_combine()
        

def usage():
    """Prints out usage in the case of no files passed"""
    print("Error: No files passed\nUsage: python3 combiner.py /path/to/csv/file1 /path/to/csv/file2 ...")

if __name__ == "__main__":
    csv_comb = CsvCombine()
    csv_comb.combine_main()

