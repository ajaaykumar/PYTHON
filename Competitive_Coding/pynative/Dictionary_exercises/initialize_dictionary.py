# dictionary exercise 4: Initialize dictionary with default values

def main(employees, defaults):
    
    resp = {i:defaults for i in employees}
    print(resp['Kelly'])


if __name__ == '__main__':
    employees = ['Kelly', 'Emma', 'John']
    defaults = {"designation": 'Application Developer', "salary": 8000}
    main(employees, defaults)

