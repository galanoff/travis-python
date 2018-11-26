def fun_tested():
    var1 = True
    if var1:
        pass
    return True


def fun_half_tested(cond):
    if cond:
        var2 = False
        return var2
    return True


def fun_not_tested():
    var3 = True
    if var3:
        pass
    return True
