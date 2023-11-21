from arnion.db.my_sql_connection import my_connection_handler


class DepartmentDataObject:
    def __init__(self, department_id=0, department_name=''):
        self.department_id = department_id
        self.department_name = department_name

class DepartmentDataHandler:
    @staticmethod
    def select_list():
        deparments = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM departments ORDER BY departments_id"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        deparments.append(DepartmentDataObject(row[0], row[1]))
            return deparments
        except:
            raise

    @staticmethod
    def select_by_id(departments_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM departments WHERE departments_id" + str(departments_id)
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    row = cursor.fetchall()
                    department = DepartmentDataHandler.get_department(row)
                    return department
        except:
            raise

        @staticmethod
        def get_department(row):
            return DepartmentDataObject(row[0], row[1])