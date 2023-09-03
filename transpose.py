import csv

def transform_csv_file(input_csv, output_csv):
    flattened_data = []

    with open(input_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        columns = list(zip(*csv_reader))  # Transpose the rows and columns
        
        for col_data in columns:
            flattened_data.extend(col_data)
            flattened_data.append('')  # Add an empty row after each column

    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Column 1'])
        csv_writer.writerows([[val] for val in flattened_data])

    print("CSV transformation complete!")

# Replace with your input and output CSV file paths
input_csv_path = "Transpose Halloween.csv"
output_csv_path = "output.csv"

transform_csv_file(input_csv_path, output_csv_path)
