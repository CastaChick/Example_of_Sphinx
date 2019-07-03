def say_hello_to(person):
    """'Hello person'を出力

    Parameters
    ----------
    person : str
        挨拶したい人の名前

    Examples
    --------
    >>> say_hello_to('Taro')
    Hello Taro

    >>> say_hello_to('Hanako')
    Hello Hanako
    """
    print('Hello ' + person)


def say_goodbye_to(person):
    """'Good bye person'を出力

    Parameters
    ---------
    person : str
        挨拶したい人の名前

    Examples
    --------
    >>> say_goodbye_to('John')
    Good bye John

    >>> say_goodbye_to('Anna')
    Good bye Anna
    """
    print('Good bye ' + person)
