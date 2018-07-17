import datetime
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')
class Employee:
    raise_amount = 1.04
    number_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@oop.com'
        Employee.number_of_employee += 1

    @classmethod
    def from_string(cls, emp_str):
        """
        this is another way of creating instance of class when provided information is string.
        :param emp_str:
        :return:
        """
        first, last, pay = emp_str.split('_')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """
        this is to find day of week
        :param day:
        :return day of week:
        """
        return day.strftime("%A")


def main():
    emp_1 = Employee("Sachin", "Tendulkar", 100000)
    emp_2 = Employee("virat", "kohali", 120000)

    emp_str_1="mahendrasingh_dhoni_110000"
    emp_str_2="youraj_singh_80000"
    #creating instance of class using class method from_string
    Employee.from_string(emp_str_1)
    Employee.from_string(emp_str_2)

    logging.debug("Number of employees are : "+str(Employee.number_of_employee))
    date=input("Please.. Enter the date(mm-dd-yyyy) to know a day of week:").strip()
    month,day,year=date.split('-')
    my_date=datetime.date(int(year),int(month),int(day))
    logging.debug("{} is {}".format(date, Employee.is_workday(my_date)))

if __name__=='__main__':
    main()







