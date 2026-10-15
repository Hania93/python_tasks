from datetime import date

task_name = input("Nazwa zadania: ")
estimated_time = int(input("Planowany czas (min): "))
priority = int(input("Priorytet: (1-3): "))

print("=== Menedżer zadań ===")
print(f"Dziś jest: {date.today()}")
print(f"Zadanie: {task_name}")
print(f"Planowany czas: {estimated_time // 60} godz. {estimated_time % 60} min")
print(f"Pilne: ", end=" ")
print("True") if priority >= 2 else print("False")


print(f"Utworzono: {date.today()}")
