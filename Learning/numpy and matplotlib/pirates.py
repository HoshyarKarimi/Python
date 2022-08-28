from csv import DictReader
from matplotlib import pyplot as plt


year = []
pirates = []
temperature = []

with open("pirates.csv", mode='r') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        year.append(row["Year"])
        pirates.append(row["Pirates"])
        temperature.append(row["Temperature"])

plt.plot(pirates, temperature, "b-o")
plt.xlabel("Pirates")
plt.ylabel("Temperature")
for i, txt in enumerate(year):
    plt.annotate(txt, (pirates[i], temperature[i]))

plt.savefig("/home/hoshyar/pirates.png")
plt.show()
