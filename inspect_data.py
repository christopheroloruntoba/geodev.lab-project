import csv

#with open('mydata.csv',encoding='utf-8-sig') as f:
#    reader = csv.DictReader(f)
 #   rows = list(reader)

#values = []
#for row in rows:
#    raw = row["area_km2"].strip()
#    if raw == "":
        continue
    values.append(float(raw))

#print("Smallest:", min(values))
#print("Largest:", max(values))
#print("Count:", len(values))




def inspect_column(mydata.csv, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []

    for row in rows:
        raw = row[column].strip()

        if raw == "":
            continue
        values.append(float(raw))

    return{
        "smallest":min(values),
        "largest":max(values),
        "count":len(values)
    }


result = inspect_column("mydata.csv", "area_km2")
print(result)


