import Employee
import pickle
mary = Employee.Employee('Mary', '89123456789', 30001)
mary.print_salary_info()
with open('data.pickle', 'wb') as f:
    pickle.dump(mary, f)
