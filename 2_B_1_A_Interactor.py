exit_code = int(input())
interactor = int(input())
checker = int(input())


def get_verdict():
    if interactor == 0:
        if exit_code != 0:
            return 3
        return checker
    elif interactor == 1:
        return checker
    elif interactor == 4:
        if exit_code != 0:
            return 3
        return 4
    elif interactor == 6:
        return 0
    elif interactor == 7:
        return 1
    return interactor


print(get_verdict())
