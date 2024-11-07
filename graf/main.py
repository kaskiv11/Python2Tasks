import numpy as np
import matplotlib.pyplot as plt

classes = ["Клас А", "Клас B", "Клас C", "Клас D"]
students = [23, 24, 32, 27]
colors = ["red", "blue", "green", "yellow"]

plt.bar(classes, students, color=colors)

plt.title("Кількість студентів у кожному класі")
plt.xlabel("Класи")
plt.ylabel("Кількість студентів")

plt.show()


nations = ["Українці", "404 ", "Білоруси", "Євреї", "Поляки", "Німці", "Молдавани", "Інші"]
peecetanges = [77.8, 17.3, 0.6, 0.2, 0.3, 0.1, 0.8, 2.9]

plt.pie(peecetanges, labels=nations)
plt.xlabel("Народи")
plt.ylabel("%")
plt.title("Народи що засиляють Україну")
plt.legend(nations, loc="upper left", bbox_to_anchor=(0.8, 0.8))
plt.axis('equal')

plt.show()


days = ["Понеділок", "Вівторок", "Середа", "Четверг", "П'ятниця", "Субота", "Неділя"]
temp = [22, 24, 21, 29, 25, 20, 27]

plt.plot(days, temp, marker='o', color="blue")
plt.xlabel("Дні")
plt.ylabel("Температура (С)")
plt.title("Зміна температури")

plt.grid(color="gray", linestyle="--", alpha=0.9)
plt.show()


x = np.linspace(-10, 10, 400)
y = (x ** 2) - 2

#plt.figure(figsize=(10, 6))
plt.plot(x, y,  marker='o')
plt.axhline(y=0, color="red", linewidth=0.5, ls='--')
plt.axvline(x=0, color="red", linewidth=0.5, ls='--')


plt.show()

