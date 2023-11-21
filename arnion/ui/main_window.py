import tkinter as tk

from arnion.data.departments_data import DepartmentDataHandler
from arnion.data.employees_data import EmployeeDataHandler
from arnion.db.my_sql_connection import ConnectionHandler


class MainWindow:

    # Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("310x380")
        self.window.title("SPAN")

        # Добавление метки заголовка
        lbl_title = tk.Label(text="SPAN",
                             font=("Helvetica", 16, "bold"),
                             fg="#0000cc",
                             justify="center")
        lbl_title.place(x=25, y=15, width=250, height=50)

        # Добавление метки заголовка данных
        lbl_title_1 = tk.Label(text="Данные",
                               font=("Helvetica", 12, "bold"),
                               fg="#0066ff",
                               justify="center")
        lbl_title_1.place(x=25, y=55, width=250, height=50)

        # Добавление кнопки данных "Отделы"
        btn_data_report = tk.Button(self.window,
                               text="Отделы",
                               font=("Helvetica", 10, "bold"),
                               bg="#ccffcc")
        btn_data_report.place(x=25, y=100, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_data_employee = tk.Button(self.window,
                                 text="Сотрудники",
                                 font=("Helvetica", 10, "bold"),
                                 bg="#ccffcc")
        btn_data_employee.place(x=160, y=100, width=120, height=50)

        # Добавление метки заголовка отчетов
        lbl_title_2 = tk.Label(text="Отчеты",
                               font=("Helvetica", 12, "bold"),
                               fg="#0066ff",
                               justify="center")
        lbl_title_2.place(x=25, y=155, width=250, height=50)

        # Добавление кнопки отчетов "Отделы"
        btn_dp_report = tk.Button(self.window,
                                  text="Отделы",
                                  font=("Helvetica", 10, "bold"),
                                  bg="#ccffcc")
        btn_dp_report.place(x=25, y=200, width=120, height=50)

        # Добавление кнопки отчетов "Сотрудники"
        btn_dp_employee = tk.Button(self.window,
                                  text="Сотрудники",
                                  font=("Helvetica", 10, "bold"),
                                  bg="#ccffcc")
        btn_dp_employee.place(x=160, y=200, width=120, height=50)


        # Добавление кнопки тест
        btn_test = tk.Button(self.window, text='Тест',
                             font=("Helvetica", 10, "bold"),
                             bg="#ffffcc",
                             command=self.do_test)
        btn_test.place(x=25, y=300, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window,
                              text="Выход",
                              font=("Helvetica", 10, "bold"),
                              bg="#ccffcc",
                              command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)

    # Функция тест
    def do_test(self):
        employees = EmployeeDataHandler.select_list()
        for employee in employees:
            print(employee.get_full_name())

    # Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()

    # Запуск цикла
    def start_mainloop(self):
        self.window.mainloop()