import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


list_of_specialty = ['Internist', 'General Practitioner', 'Dentist', 'Family Physician', 'Pediatrician', 'Obstetrician and Gynecologist']
list_of_rates = [4.11329966683179, 1.8228235317679014, 4.527576601936957, 4.408991234867196, 4.38193833145276, 4.458854173620542]
width = 0.4
plt.bar(list_of_specialty, list_of_rates, width, align='center')
plt.xticks(list_of_specialty,list_of_specialty,rotation='80')
ax = plt.axes()
plt.xlabel('Speciality', fontsize=16)
plt.ylabel('Rate', fontsize=16)
minor_ticks = np.arange(0, 5, 0.2)
major_ticks = np.arange(0, 6, 1)
ax.set_yticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
plt.grid(True, lw = 0.8, ls = '--', c = '.75')
plt.title('Average rate of doctors in each speciality')
plt.savefig('speciality.png', bbox_inches = "tight")
plt.show()