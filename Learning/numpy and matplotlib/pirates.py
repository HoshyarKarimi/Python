from csv import DictReader
from matplotlib import pyplot as plt


year = []
pirates = []
temperature = []

with open("pirates.csv", mode='r') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        year.append(int(row["Year"]))
        pirates.append(int(row["Pirates"]))
        temperature.append(float(row["Temperature"]))

plt.plot(pirates, temperature, "b-o")
plt.title("Global temperature as a function of pirate population")
plt.xlabel("Total pirates")
plt.ylabel("Average global temperature (Celsius)")
plt.axis([-300, 48000, 14, 16])
for i, txt in enumerate(year):
    plt.annotate(txt, (pirates[i], temperature[i]))

plt.savefig("/home/hoshyar/pirates.png")
plt.show()
