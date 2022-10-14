def kerdest_feltesz(kerdes, helyes_valasz):
    valasz = input(kerdes)
    if valasz == helyes_valasz:
        print('A valasz helyes')
        return True
    else:
        print('A válasz helytelen')
        return False