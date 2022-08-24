sukupuoli = input('Sukupuolesi: ')
hemo = int(input('Anna hemoglobiini(g/l): '))

if sukupuoli.upper() == 'NAINEN':
    if hemo < 117:
        print('LIIAN ALHAINEN HANKI APUA HETI APUAAAA')
    elif 117 <= hemo <= 175:
        print('NORMAALIA ON JUUH')
    else:
        print('LIIAN KORKIA HUHHHUUUH')

elif sukupuoli.upper() == 'MIES':
    if hemo < 134:
        print('LIIAN ALHAINEN HANKI APUA HETI APUAAAA')
    elif 134 <= hemo <= 195:
        print('NORMAALIA ON JUUH')
    else: print('LIIAN KORKIA HUHHHUUUH')
else:
    print('Sori mutta tää koodi ei oo tarpeeks advanced')