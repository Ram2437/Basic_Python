'''
  * Checking whether phone numbers of a given employee are valid - get_invalid_phone_count
  * Function should take 2 arguments, employee_id and phone_numbers (variable number)
  * Check whether each phone number have 10 digits.
  * Return employee_id and number of phone numbers with less than 10 digits
'''

def get_invalid_phone_count(employee_id, *phone_numbers):
    invalid_count=0
    for phone_number in phone_numbers:
        if len(phone_number)!=10:
            invalid_count += 1
    return(employee_id, invalid_count)

employee_id,invalid_count = get_invalid_phone_count(1, '1234567890','123', '447')
# print( "Employee {} has {} phones".format(employee_id, invalid_count))

'''
  * Adding employee (add_employee)
  * Function should take employee_id, employee_name, salary and phone_numbers (variable number), degrees (variable keyword arguments) as arguments.
  * Degrees should be with specialization. There can be one or more degrees with specializations with keys bachelors, masters, executive, doctorate.
  * Make sure salary is defaulted to 3000. If salary is passed and if it is less than 3000 throw exception with message “Invalid Salary, Salary should be at least 3000”
  * Call get_invalid_phone_count and check if it is greater than 0. If invalid phone count is greater than 0, throw an exception with message “One or more phone number of an employee is not valid”
  * Get count of degrees by processing variable keyword argument
  * If there are no exceptions print “Employee {employee_id} with {number} of degrees is successfully added”
'''
def add_employee(employee_id, employee_name, *phone_numbers, salary=3000, **degrees):
    '''
    Paramenters can be named as p_ and variables as l_ for a better naming convention
    employee_id:
    employee_name:
    phone_numbers: '*' represents we can pass multiple arguments
    salary:
    degrees:  '**' represents we can pass multiple key word arguments
    '''
    degree_types = ('Bachelors', 'Masters', 'Executive', 'Doctorate')
    try:
        l_employee_id, l_invalid_count = get_invalid_phone_count(employee_id, *phone_numbers)
        if l_invalid_count != 0 or salary < 3000:
            raise ValueError

        for degree_key in degrees:
            if degree_key not in degree_types:
                raise ValueError
        print("Employee {} with {} of degrees is successfully added and his salary is {}".format(employee_id, len(degrees), salary))

    except ValueError as ve:
        print("One or more phone number of an employee is not valid or Invalid salary, salary should be atleast 3000 or the degree is not correct")


add_employee(1, 'Ram', '1234567890', salary=3000, Bachelors= 'B. Sc', Masters = 'MS' )