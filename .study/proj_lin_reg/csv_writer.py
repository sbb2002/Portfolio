import csv

def save_to_file(inputs):
    file = open("cost_data.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["DATE", "COST"])
    for i in inputs:
        writer.writerow(list(i.values()))
    file.close()
    return