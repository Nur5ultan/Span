import tkinter as tk

from arnion.data.departments_data import DepartmentDataHandler, DepartmentDataObject
from arnion.data.employees_data import EmployeeDataHandler, EmployeeDataObject
from arnion.db.mysql_connection import ConnectionHandler
from arnion.ui.departments_data_ui import DepartmentsWindow
from arnion.ui.departments_reports_ui import DepartmentsReportWindow
from arnion.ui.employees_data_ui import EmployeesWindow
from arnion.ui.employees_reports_ui import EmployeesReportWindow


class MainWindow:
    # Конструктор
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("310x380")
        self.window.title("SPAN")

        # Добавление метки заголовка
        lbl_title = tk.Label(
            text="SPAN", font=("Helvetica", 16, "bold"), fg="#0000cc", justify="center"
        )
        lbl_title.place(x=25, y=15, width=250, height=50)

        # Добавление метки заголовка данных
        lbl_subtitle_data = tk.Label(
            text="Данные",
            font=("Helvetica", 12, "bold"),
            fg="#0066ff",
            justify="center",
        )
        lbl_subtitle_data.place(x=25, y=55, width=250, height=50)

        # Добавление кнопки данных "Отделы"
        btn_list_departments = tk.Button(
            self.window,
            text="Отделы",
            font=("Helvetica", 10, "bold"),
            bg="#ccffcc",
            command=self.do_list_departments,
        )
        btn_list_departments.place(x=25, y=100, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_list_employees = tk.Button(
            self.window,
            text="Сотрудники",
            font=("Helvetica", 10, "bold"),
            bg="#ccffcc",
            command=self.do_list_employees,
        )
        btn_list_employees.place(x=160, y=100, width=120, height=50)

        lbl_subtitle_report = tk.Label(
            text="Отчёт",
            font=("Helvetica", 12, "bold"),
            fg="#0066ff",
            justify="center",
        )
        lbl_subtitle_report.place(x=25, y=155, width=250, height=50)

        # Добавление кнопки отчетов "Отделы"
        btn_report_department = tk.Button(
            self.window,
            text="Отделы",
            font=("Helvetica", 10, "bold"),
            bg="#ccffcc",
            command=self.do_report_departments,
        )
        btn_report_department.place(x=25, y=200, width=120, height=50)

        # Добавление кнопки отчетов "Сотрудники"
        btn_report_employee = tk.Button(
            self.window,
            text="Сотрудники",
            font=("Helvetica", 10, "bold"),
            bg="#ccffcc",
            command=self.do_report_employees,
        )
        btn_report_employee.place(x=160, y=200, width=120, height=50)

        # Добавление кнопки "Тест"
        btn_test = tk.Button(
            self.window,
            text="Тест",
            font=("Helvetica", 10, "bold"),
            bg="#ffffcc",
            command=self.do_test,
        )
        btn_test.place(x=25, y=300, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(
            self.window,
            text="Выход",
            font=("Helvetica", 10, "bold"),
            bg="#ccffcc",
            command=self.close,
        )
        btn_close.place(x=160, y=300, width=120, height=50)

    # Функция 'Тест'
    def do_test(self):
        employee = EmployeeDataObject(
            first_name="Ирина",
            middle_name="Анатольевна",
            last_name="Сергеева",
            department_id=3,
        )
        print(employee.employee_id)
        EmployeeDataHandler.insert(employee)
        print(employee.employee_id)
        print("Готово!")

    # Открытия списка "Отделы"
    def do_list_departments(self):
        rpt = DepartmentsWindow()
        rpt.open()

    # Открытия списка "Сотрудники"
    def do_list_employees(self):
        rpt = EmployeesWindow()
        rpt.open()

    # Открытие отчета "Отделы"
    def do_report_departments(self):
        rpt = DepartmentsReportWindow()
        rpt.open()

    # Открытие отчета "Сотрудники"
    def do_report_employees(self):
        rpt = EmployeesReportWindow()
        rpt.open()

    # Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()

    # Запуск цикла
    def start_mainloop(self):
        self.window.mainloop()
