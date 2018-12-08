from peewee import *
from employee import db
from employee import Employee
from payroll import Payroll

class Cheque(Model):
    Cheque_date=FloatField
    Cheque_amount=FloatField
    employee_id = ForeignKeyField(Employee, to_field="id", on_update="cascade")

    class Meta:
        database =db
        table_name = 'Cheque'

Cheque.create_table(fail_silently=True)
