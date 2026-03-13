#########################################################FUNCTIONS#######################################################



#                                         Creating a function
# ======================================================================================================
# 1) function header always starts with def keyword, which indicates that this is a function definition
# 2) then comes the function name, which follows the same naming conventions as variables
# 3) immediately after the name are parentheses that may include arguments separated by commas,
#    arguments or parameters are values that are passed in as inputs when the function is called and used
#    in the function body, if a function doesn't take arguments, these parentheses are left empty
# 4) header always end with a colon:



# Example of creating a function
# def function_name(optional, arguments):



# Defining Functions
def cylinder_volume(height, radius):
    pi = 3.15159
    return height * pi * radius**2



# Default Arguments
# we can add default arguments in a function to have default values for
# parameters that are unspecified in a function call
def rectangular_prism_volume(length, width, height = 5): # height is set to 5 if not specified
    return length * width * height



# Variable Scope
# - variable scope refers to which parts of a program a variable can be referenced, or used from
# - if a variable is created inside a function, it can only be used within that function
# - you can use the same name for different variables that are used in different functions
# - variables defined outside the functions, can be accessed within a function (GLOBAL SCOPE)



# Documentation
# Docstring: a type of comment used to explain the purpose of a function and how it should be used
# Example:
"""Docstring"""
"""summary of function
    input(arguments)
    output"""



# Main Function
if __name__ == '__main__':
    # calling a function
    cylinder = cylinder_volume(10, 3)
    print(cylinder)
    
    
    
    # calling a function with default argument
    print(rectangular_prism_volume(2, 4, 5)) # specifying all parameter values
    print(rectangular_prism_volume(2, 4)) # omitted height, so height = 5
    print(rectangular_prism_volume(2, 4, 10)) # 10 will overwrite the default value of 5
    
    
    
    # Lambda Expressions
    # you can use lambda expressions to create anonymous functions(functions that don't have a name)
    multiply = lambda x,y: x*y
    print(multiply(4, 7)) # calling multiply
    # || (showing that the above lambda expression is the same as the function below)
    # def multipy(x, y):
    #	return x*y
    # in either case we can call multiply like this: multiply(4, 7)
    
    
    
    #                                 Components of a Lambda Function
    # ===============================================================================================
    # 1) the lambda keyword is used to indicate that this is a lambda expression
    # 2) following the lambda are 1 or more arguments for the anonymous function separated by commas,
    #    followed by a colon:
    # 3) last is an expression that is evaluated and returned in this function
    
    
    
    # Example of creating a lambda function
    # lambda 1 or, more arguments: expression that is evaluated and returned