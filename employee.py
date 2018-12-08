from peewee import *
from flask import url_for

try:
    db = PostgresqlDatabase('d4nss17661naok', user='eoanplhpoqddlc', password='3f8e9557d48a236077cc1d1faeab85c9f3ce42ea852abd8f0076b39fd4fa94b6', host='ec2-54-235-133-42.compute-1.amazonaws.com')
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