'''
## **5. Validate Email Format**

**Concepts:** functions, strings, conditionals

👉 Create a function:
```python
def is_valid_email(email):
```

👉 What it should do:
* Check if an email is “valid” based on simple rules
* Return `True` or `False`

---

## ✅ Rules to check
Your function should verify that:
* Contains **exactly one `@`**
* Has at least one `.` after the `@`
* `@` is **not the first or last character**

---

## 👉 Example
```text
Input: "test@gmail.com" → Output: True  
Input: "testgmail.com" → Output: False  
Input: "@gmail.com" → Output: False  
```

---

## 🔹 Hints
* Use:
```python
email.count('@')
```
* Split the email:
```python
parts = email.split('@')
```
* Check the domain part (after `@`) for `.`

---

## 🔹 Challenge
Make it stricter:
* No spaces allowed
* Must end with something like `.com`, `.org`, `.edu`
* No multiple `@`

---

## 🚀 Bonus (real-world thinking)
In real apps, email validation is more complex, but this teaches:
* Input validation
* String parsing
* Breaking problems into steps
'''

# define function to check if user inputted a valid email
# email is a string
# function returns True or False
def is_valid_email(email):
    # boolean to check if email inputted is valid
    # assume email inputted isn't valid (False)
    is_valid = False

    # RULES TO CHECK
    # email.count('@') is a string method in Python that counts how many times a specific character appears in a string**************************
    # checks if @ appears exactly 1 time
    if email.count('@') == 1:
        # email.split('@') splits the string into a list using '@' as the separator**************************
        # email_in_list[0] -> username
        # email_in_list[1] -> domain
        '''EX. email = cathy@gmail.com
               email_in_list = email.split('@') -> output: ['cathy', 'gmail.com']
                                                       username^      domain^
                                                    email_in_list[0]  email_in_list[1]'''
        email_in_list = email.split('@')
        # checks if . in the second element in email_in_list
        if '.' in email_in_list[1]:
            # checks if the first and last string of email (user input) is not @
            if email[0] != '@' and email[-1] != '@':
                # checks if email string has spaces
                if ' ' not in email:
                    # checks if .com, .org, or .edu is in the second element in email_in_list
                    if '.com' in email_in_list[1] or '.org' in email_in_list[1] or '.edu' in email_in_list[1]:
                        # all these checks are passed, is_valid -> True
                        is_valid = True

    # return True or False depending if email is valid or not
    return is_valid

# define function to get user input, call function, and display output
def main():
    # get email from user
    user_email = input('Enter in an email: ')
    # call is_valid_email(email) function
    # pass in user_email (string)
    # valid holds a boolean, if email is valid -> True, if email is invalid -> False
    valid = is_valid_email(user_email)

    # user inputted a valid email
    if valid == True:
        print('{} is a valid email'.format(user_email))
    # user did not input a valid email
    else:
        print('{} is not a valid email'.format(user_email))

# calls main() function
if __name__ == '__main__':
    main()


'''
def is_valid_email(email):
    is_valid = False

    if email.count('@') == 1:
        email_in_list = email.split('@')
        if '.' in email_in_list[1]:
            if email[0] != '@' and email[-1] != '@':
                if ' ' not in email:
                    if '.com' in email_in_list[1] or '.org' in email_in_list[1] or '.edu' in email_in_list[1]:
                        is_valid = True

    return is_valid

def main():
    user_email = input('Enter in an email: ')
    valid = is_valid_email(user_email)

    if valid == True:
        print('{} is a valid email'.format(user_email))
    else:
        print('{} is not a valid email'.format(user_email))

if __name__ == '__main__':
    main()
    '''