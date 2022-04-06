# csv libraries also include pandas, openpyxl, and google sheets python api
import csv

data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(len(data_lines))
for line in data_lines[:5]:
    print(line)
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1] + " " + line[2])
print(full_names)
file_to_output = open("to_save_file.csv", mode="w", newline="")
csv_writer = csv.writer(file_to_output, delimiter=",")
csv_writer.writerow(["a", "b", "c"])
csv_writer.writerows([["1", "2", "3"], ["4", "5", "6"]])
file_to_output.close()
f = open("to_save_file.csv", mode="a", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["a", "b", "c"])
f.close()
