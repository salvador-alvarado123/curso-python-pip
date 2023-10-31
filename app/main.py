import utils
import charts
import read_csv



def run():
  data = read_csv.read_csv("data.csv")
  data = list(filter(lambda item: item["Continent"] == "South America", data))

  country = list(map(lambda x: x["Country/Territory"], data))
  percentaje = list(map(lambda x: x["World Population Percentage"], data))

  charts.generate_pie_chart(country, percentaje)


  country = input("Ingresa tu pais => ")
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"], labels, values)





if __name__ == "__main__":
  run()
  

