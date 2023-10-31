def get_population(country_dict):
  population_dict = {
    "A 2022": int(country_dict["2022 Population"]),
    "A 2020": int(country_dict["2020 Population"]),
    "A 2015": int(country_dict["2015 Population"]),
    "A 2010": int(country_dict["2010 Population"]),
    "A 2000": int(country_dict["2000 Population"]),
    "A 1990": int(country_dict["1990 Population"]),
    "A 1980": int(country_dict["1980 Population"]),
    "A 1970": int(country_dict["1970 Population"])
  }

  
  labels = population_dict.keys() 
  values = population_dict.values()
  return labels, values


def population_by_country(data, country):
  result = list(filter(lambda x: x["Country/Territory"] == country, data))
  return result

