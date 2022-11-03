def sorbarendez(szoveg):
    return ' '.join(sorted(szoveg.split()))

print(sorbarendez('banan alma narancs'))
print(sorbarendez('ember állat étel ital alma')) # ékezetet nem jól kezeli