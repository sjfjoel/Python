#1 eval function converts a str to an expression - 10+50-5 

expr = input("Enter an expression : ")
result = eval(expr)
print(expr," : ",type(expr))
print(result)

#2 eval function converts a str to respected datatype

id, name, salary, contact = [eval(x) for x in input("Enter the employee ID, Name, Salary, Contact : ").split(',')] # give name inside ""
print("ID : ",id," : ",type(id))
print("ID : ",name," : ",type(name))
print("ID : ",salary," : ",type(salary))
print("ID : ",contact," : ",type(contact))