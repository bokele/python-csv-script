import csv


def write_to_file(filename, data_chuck, data_header=None):
    with open(filename, 'w') as new_file:
        writer = csv.writer(new_file)
        if data_header:
            writer.writerow(data_header)
        writer.writerows(data_chuck)


def split_to_csv(filename, row_count):
    chunk = []
    file_number = 1
    row_number = 0
    header = ''
    original_name,extension = filename.split('.')
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if header == '':
                header = row
                continue
            chunk.append(row)
            row_number += 1
            if row_number > row_count:
                write_to_file(f'{original_name}-{file_number}.{extension}', chunk, header)
                chunk = []
                file_number += 1
                row_number = 0

        if chunk:
            write_to_file(f'{original_name}-{file_number}.{extension}', chunk, header)
