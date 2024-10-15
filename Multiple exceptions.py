try:
    num1,num2=eval(input("enter two numbers,separeted by comma:"))
    result=num1/num2
    print("Result is",result)

#using multiple except block for diffrent types of error
except ZeroDivisionError:
    print("division by zero is error")

except SyntaxError:
    print("comma is missing.put the numbers like this:1,2.")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("This will execute no matter what")
  