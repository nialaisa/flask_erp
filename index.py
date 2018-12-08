from employee import Employee
from payroll import Payroll
from payroll_calculator import Payrollcalculator
from cheque import Cheque

from flask import Flask, render_template, request, redirect, url_for


app=Flask(__name__)

x=2

@app.route("/")
def home():
    allemployees=Employee.select()
    return render_template("index1.html", displayEmployees=allemployees)

@app.route("/employee")
def employee():
    return render_template("add_employee.html")


@app.route("/saveEmployee", methods=['POST'])
def saveEmployee():
    name = request.form["form_full_name"]
    kra = request.form["form_kra_pin_number"]
    department = request.form["form_department"]
    position = request.form["form_position"]
    basic = request.form["form_basic_salary"]
    house = request.form["form_house_allowance"]

    Employee.create(full_name=name,
                    kra_pin=kra,
                    department=department,
                    position=position,
                    basic_salary=basic,
                    house_allowance=house)
    return redirect(url_for("home"))

@app.route("/updateEmployee/<me>", methods=["POST"])
def update(me):
    return str(me)

#Fetch employee  using id

    emp=Employee.select().where(Employee.id == int(me)).get()
    #update employee details
    emp.full_name = request.form["form_full_name"]
    emp.kra = request.form["form_kra_pin_number"]
    emp.department = request.form["form_department"]
    emp.position = request.form["form_position"]
    emp.basic = request.form["form_basic_salary"]
    emp.house = request.form["form_house_allowance"]
    emp.save()
    return redirect(url_for ("home"))
#fetch the user
#object.delete

@app.route("/deleteEmployee/<int:me>", methods=["GET"])
def delete(me):
    emp = Employee.select().where(Employee.id == int(me)).get()
    emp.delete_instance()
    return str(me)

#payroll routes

@app.route("/payroll/<int:me>")
def payroll(me):
    allpayrolls=Payroll.select().join(Employee).where(Employee.id==int(me))
    return render_template('payroll2.html',mypayrolls=allpayrolls, employeeId=me)

@app.route("/payroll/add", methods=["POST"])
def payroll2():
    benefits=request.form["form_other_benefits"]
    Date=request.form["form_date"]
    overtime=request.form["form_overtime"]
    employee_id=request.form['form_empdata_id']
    empdata=Employee.select().where(Employee.id==employee_id).get()
    calc=Payrollcalculator(empdata.basic_salary, overtime, empdata.house_allowance, benefits)
    Payroll.create(benefits=benefits,
                   payroll_date=Date,
                   overtime=overtime,
                   nhif=calc.nhif,
                   nssf=calc.nssf,
                   payee=calc.payee,
                   employee_id=employee_id)

    return redirect(url_for('payroll2'))


@app.route("/cheque/add", methods=["POST"])
def cheque():
    Date=request.form["form_date"]
    employee_id=request.form['form_empdata_id']
    empdata=Employee.select().where(Employee.id==employee_id).get()

    return redirect(url_for (cheque))


if __name__== "__main__":
    app.run(debug=True)
