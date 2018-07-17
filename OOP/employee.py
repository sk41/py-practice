import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')
class Employee:
    raise_amount=1.04
    number_of_employee=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@oop.com'
        Employee.number_of_employee+=1

    def show_info(self):
        """
        to show employee information
        :return none:
        """
        logging.debug("employee full name:{0} {1}".format(self.first,self.last))
        logging.debug("Email id :{0}".format(self.email))
        logging.debug("{0}'s raised payment is : {1}\n".format(self.first,(self.pay*self.raise_amount)))

def main():
    emp_1=Employee("Sachin","Tendulkar",100000)
    emp_2=Employee("virat","kohali",120000)
    logging.debug("Total number of employees: {0}".format(Employee.number_of_employee))
    emp_1.show_info()
    emp_2.show_info()

if __name__=='__main__':
    main()




