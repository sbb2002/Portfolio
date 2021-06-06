import csv

def save_to_file(inputs):
    file = open(r"proj_lin_reg\data\raw.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["date", "season", "avgTemp", "minTemp", "maxTemp", "rainfall", "interest", "cost"])
    for i in inputs:
        writer.writerow(list(i.values()))
    file.close()
    return