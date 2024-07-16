import matplotlib.pyplot as plt

# Extending the data with birth and death locations
imams = [
    {"name": "Imam Abu Hanifah", "birth": 699, "death": 767, "birthplace": "Kufa, Irak", "deathplace": "Baghdad, Irak"},
    {"name": "Imam Malik bin Anas", "birth": 711, "death": 795, "birthplace": "Madinah, Arab Saudi", "deathplace": "Madinah, Arab Saudi"},
    {"name": "Imam Syafi'i", "birth": 767, "death": 820, "birthplace": "Gaza, Palestina", "deathplace": "Fustat, Mesir"},
    {"name": "Imam Ahmad bin Hanbal", "birth": 780, "death": 855, "birthplace": "Baghdad, Irak", "deathplace": "Baghdad, Irak"}
]

plt.figure(figsize=(14, 6))

for imam in imams:
    plt.plot([imam['birth'], imam['death']], [imam['name'], imam['name']], marker='o')
    plt.text(imam['birth'] - 2, imam['name'], f"{imam['birth']} ({imam['birthplace']})", va='center', ha='right', fontsize=9, color='blue')
    plt.text(imam['death'] + 2, imam['name'], f"{imam['death']} ({imam['deathplace']})", va='center', ha='left', fontsize=9, color='red')

# Adding labels and titles
plt.xlabel('Year')
plt.title('Timeline of the Lives of the Four Imams with Birth and Death Places')
plt.yticks(range(len(imams)), [imam['name'] for imam in imams])
plt.grid(True)
plt.xlim(650, 900)

# Showing the plot
plt.show()
