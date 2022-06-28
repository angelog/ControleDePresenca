import sqlite3
from sqlite3 import Error

#Gerenciamento do Banco
class DataBase:

    def __init__(self):
        try:
            self.database = sqlite3.connect('database.db')
        except Error as e:
            print(e)
        cursor = self.database.cursor()
        cursor.execute('Create table if not exists Alunos('
                       'Rg int(12) primary key,'
                       'Nome varchar(100) not null,'
                       'Tel varchar(12),'
                       'Responsavel varchar(100) not null'
                       ')')
        cursor.execute('Create table if not exists Presenca('
                       'Rg int(12),'
                       'Data datetime'
                       ')')

    def insert(self, table, data):
        cursor = self.database.cursor()

        columns = '('
        values = '('
        for column in data:
            columns += column + ','
            values += "'{}',".format(data[column])

        if table == 'Alunos':
            columns = columns[:-1] + ')'
            values = values[:-1] + ')'

        elif table == 'Presenca':
            columns = columns + 'Data)'
            values = values + "DateTime('now','localtime'))"

        query = f'insert into {table} {columns} values {values}'
        print(query)
        cursor.execute(query)
        self.database.commit()


if __name__ == '__main__':
    DataBase()
