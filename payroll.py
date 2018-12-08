from peewee import *
from employee import db
from employee import Employee

class Payroll (Model):
    payroll_date=DateField()
    overtime=FloatField()
    other_benefits=FloatField()
    nssf=FloatField()
    nhif=FloatField()
    payee=FloatField()
    employee_id=ForeignKeyField(Employee, to_field="id", on_update="cascade")

    class Meta:
        database = db
        table_name='payroll'
Payroll.create_table(fail_silently=True)