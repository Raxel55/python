import pickle
with open('data.pickle', 'rb') as f:
    new_mary = pickle.load(f)
new_mary.print_salary_info()
