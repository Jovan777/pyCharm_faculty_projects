def kako_da_idem_do_tamo(miles):
    if miles>=120:
        return 'Idi avionom'
    elif miles>=20:
        return 'Idi kolima'
    else:
        return 'Pesaci'

put=kako_da_idem_do_tamo(800)
print(put)
