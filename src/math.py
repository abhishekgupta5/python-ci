class Math():
    def add_integers(val1, val2):
        if not isinstance(val1, int) and not isinstance(val2, int):
            return 'This method only adds integers. Try Again.'
        else:
            return val1 + val2
