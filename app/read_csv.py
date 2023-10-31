import csv

def read_csv(path):
  with open(path, "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=",")
    columna = next(lector)
    data = []
    for row in lector:
      iterable = zip(columna, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    
    return data
      

if __name__ == "__main__":
  r = read_csv("./app/data.csv")
  print(r[0])
  print(r[1])

#for row in lector:
#print("****" * 5)
#print(row)