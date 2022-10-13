"""Decorators are syntactic sugar for function which take function as argument and does some pre/post execution and returns the function"""

# Execution sequence of decorators
print("\n\n UNDERSTANDING OF DECORATOR \n\n")


def decorator(func):
    print("\t> Main Decorator")

    def wrapper(*args, **kwargs):
        print("\t\t>> in wrapper")
        print("\t\t>> args", args)
        print("\t\t>> kwargs", kwargs)
        func(*args, **kwargs)  # need to return if function returns something
        print("\t\t>> Execution completed within wrapper")

    print("\t> Execution of Decorator done at the moment when it's call. But not of wrapper")
    return wrapper  # needs to be return or else it will execute directly


@decorator  # will execute lines in decorator = decorator(child_fun)
def child_fun(one, two, three, four):
    print(f"\t\t\t>>> argument: {one, two, three,four}")
    print("\t\t\t>>> In child function")


child_fun(1, 2, 3, four=4)
# OUTPUT
"""
UNDERSTANDING OF DECORATOR
        > Main Decorator
        > execution complete of decorator. But not of wrapper function
                >> in wrapper
                >> args (1, 2, 3)
                >> kwargs {'four': 4}
                        >>> argument: (1, 2, 3, 4)
                        >>> In child function
                >> Execution completed within wrapper
"""

# USE CASE
class Author:
    def __init__(self, name) -> None:
        self.name = name
        self.logged_in = False


def is_authenticated(func):
    def wrapper(user):
        func(user) if user.logged_in else print(403)

    return wrapper


# this will pass blog function as argument to is_authenticated function
@is_authenticated
def blog(user):
    print(f"Blog by {user.name}")


author = Author("Writer")
blog(author)  # 403

author.logged_in = True
blog(author)  # Blog by Writer

# -----------------------------------------------
# without using decorator (syntactic sugar)
def like(user):
    print(f"Blog liked by {user.name}")


# just like using decorator
auth_like = is_authenticated(like)
author_2 = Author("Auth")
auth_like(author_2)  # 403

author_2.logged_in = True
auth_like(author_2)  # Blog liked by Auth
