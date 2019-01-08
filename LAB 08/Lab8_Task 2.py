print("Muhammad Osama   18b-003-cs  CS-(A)")
print("Lab-08   28/12/2018")
print("Programming Exercise: Q-2")
"""2. Assuming that variable forecast has been assigned string 'It will be a sunny day today'
Write Python statements corresponding to these assignments:
(a) To variable count, the number of occurrences of string 'day' in string forecast.
(b) To variable weather, the index where substring 'sunny' starts.
(c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'."""
forecast = 'It will be a sunny day today'
print(forecast.count('day'))
print(forecast.find('sunny'))
print(forecast.replace('sunny','cloudy'))