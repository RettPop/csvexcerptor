import argparse

#   <input file>
#   <output file>
#   series of <column_name:value> parameters,
#   series of <source_column:new_column_name>
#   [dst_id_column_name:dst_id_value]
# reads input file looking for a row with given columns value
# takes value of the source_column of the row
# open/create output_file
# add to the file value from the source_column of input_file to the new_column_name column
# add to output_file dst_id_column_name column with dst_id_value value
# prints the line to output file or to stdout
# throw if output_file exists and contains any of dst_column's.
# throw if output_file exists and contains more than 1 values row

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser("Extracts specified cells from input CSV file")
    args_parser.add_argument("-i", "--input-file", dest="input_file", action="store")
    args_parser.add_argument("-o", "--output-file", dest="output_file", action="store")
    args_parser.add_argument("-s", "--src-col-value", dest="source_cells", action="append")
    args_parser.add_argument("-d", "--dst-columns", dest="dst_columns", action="append")
    args_parser.add_argument("-c", "--id-column", dest="id_column", action="store")
    args_parser.add_argument("-v", "--id-value", dest="id_value", action="store")

    # args = args_parser.parse_args(["-id", "'Col name':'host name'", "--src-col-value", "1-2", "--src-col-value", "1:2", "--dst-columns", "1:2"])
    args = args_parser.parse_args()
    print(args)
