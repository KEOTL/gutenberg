def isDate(string):
    try:
        parse(string);
        return True;
    except ValueError:
        return False;
