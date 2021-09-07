def anketa(*args, **kwargs):
    """
    :return: one line with all user's info (FIO, bday, city, tel, email
    """
    name = input("what is your name: ")
    surname = input("what is your surname: ")
    bday = input("what is your bday: ")
    city = input("what is your city: ")
    tel = input("what is your phone: ")
    email = input("what is your email: ")
    print(f"name - {name}; surname - {surname}; bday - {bday}; city - {city}; tel - {tel}; email - {email}")
    #return(**kargs)


anketa()
