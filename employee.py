from peewee import *
from flask import url_for

try:
    db = PostgresqlDatabase('payrollsystem', user='postgres', password='./', host='localhost')
    print("succesful connection")

except:
    print('unsuccessful connection')

class Employee(Model):
    id=PrimaryKeyField
    full_name=CharField()
    kra_pin=CharField()
    department=CharField()
    position=CharField()
    basic_salary=FloatField()
    house_allowance=FloatField()


    class Meta:
        database = db
        table_name='employees'
Employee.create_table(fail_silently=True)