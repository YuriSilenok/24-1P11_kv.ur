import tkinter as tk
from tkinter import messagebox
import math

def calculate_roots():
    try:
        # Получаем коэффициенты из полей ввода
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        # Вычисляем дискриминант
        discriminant = b**2 - 4*a*c
        
        if discriminant > 0:
            # Два действительных корня
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            result = f"Корни: x₁ = {x1:.2f}, x₂ = {x2:.2f}"
        elif discriminant == 0:
            # Один корень
            x = -b / (2*a)
            result = f"Один корень: x = {x:.2f}"
        else:
            # Комплексные корни
            real_part = -b / (2*a)
            imag_part = math.sqrt(abs(discriminant)) / (2*a)
            result = f"Комплексные корни: {real_part:.2f} ± {imag_part:.2f}i"
        
        # Выводим результат
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа корректно!")

# Создаем окно
root = tk.Tk()
root.title("Калькулятор квадратного уравнения")
root.geometry("400x300")

# Поля для ввода коэффициентов
tk.Label(root, text="Коэффициент a:").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Коэффициент b:").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Коэффициент c:").pack(pady=5)
entry_c = tk.Entry(root)
entry_c.pack()

# Кнопка "Рассчитать"
btn_calculate = tk.Button(root, text="Рассчитать", command=calculate_roots)
btn_calculate.pack(pady=10)

# Метка для вывода результата
label_result = tk.Label(root, text="Результат: ")
label_result.pack()

root.mainloop()