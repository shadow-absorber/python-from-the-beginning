antal_sockerkakor = int(input("Hur många sockerkakor vill du baka? "))
if antal_sockerkakor <= 0:
    print("Måste baka minst en sockerkaka!")
else:
    # bass värden för sockerkaka
    ägg = 3  # st
    strösocker = 3  # dl
    vaniljsocker = 2  # tsk
    bakpulver = 2  # tsk
    vetemjöl = 3  # dl
    smör = 75  # g
    vatten = 1  # dl
    # print start
    print("===========================================")
    print(f"Sockerkaka, {antal_sockerkakor} sats")

    # ägg räkning
    antal_ägg = ägg * antal_sockerkakor
    print(f"{antal_ägg} st ägg")

    # strösocker räkning
    mängd_strösocker = strösocker * antal_sockerkakor
    if mängd_strösocker >= 10:
        mängd_strösocker_liter = mängd_strösocker // 10
        mängd_strösocker_dl = mängd_strösocker % 10
        print(f"{mängd_strösocker_liter} L och {mängd_strösocker_dl} dl strösocker")
    else:
        print(f"{mängd_strösocker} dl strösocker")
    # vaniljsocker räkning
    mängd_vaniljsocker = vaniljsocker * antal_sockerkakor
    if mängd_vaniljsocker >= 200:
        mängd_vaniljsocker_liter = mängd_vaniljsocker // 200
        mängd_vaniljsocker = mängd_vaniljsocker % 200
        mängd_vaniljsocker_dl = mängd_vaniljsocker // 20
        mängd_vaniljsocker = mängd_vaniljsocker % 20
        mängd_vaniljsocker_msk = mängd_vaniljsocker // 3
        mängd_vaniljsocker = mängd_vaniljsocker % 3
        print(f"{mängd_vaniljsocker_liter} L, {mängd_vaniljsocker_dl} dl, {mängd_vaniljsocker_msk} msk, och {mängd_vaniljsocker} tsk vaniljsocker")
    elif mängd_vaniljsocker >= 20:
        mängd_vaniljsocker_dl = mängd_vaniljsocker // 20
        mängd_vaniljsocker = mängd_vaniljsocker % 20
        mängd_vaniljsocker_msk = mängd_vaniljsocker // 3
        mängd_vaniljsocker = mängd_vaniljsocker % 3
        print(f"{mängd_vaniljsocker_dl} dl, {mängd_vaniljsocker_msk} msk, och {mängd_vaniljsocker} tsk vaniljsocker")
    elif mängd_vaniljsocker >= 3:
        mängd_vaniljsocker_msk = mängd_vaniljsocker // 3
        mängd_vaniljsocker = mängd_vaniljsocker % 3
        print(f"{mängd_vaniljsocker_msk} msk, och {mängd_vaniljsocker} tsk vaniljsocker")
    else:
        print(f"{mängd_vaniljsocker} tsk vaniljsocker")

    # bakpulver räkning
    mängd_bakpulver = bakpulver * antal_sockerkakor
    if mängd_bakpulver >= 200:
        mängd_bakpulver_liter = mängd_bakpulver // 200
        mängd_bakpulver = mängd_bakpulver % 200
        mängd_bakpulver_dl = mängd_bakpulver // 20
        mängd_bakpulver = mängd_bakpulver % 20
        mängd_bakpulver_msk = mängd_bakpulver // 3
        mängd_bakpulver = mängd_bakpulver % 3
        print(f"{mängd_bakpulver_liter} L, {mängd_bakpulver_dl} dl, {mängd_bakpulver_msk} msk, och {mängd_bakpulver} tsk bakpulver")
    elif mängd_bakpulver >= 20:
        mängd_bakpulver_dl = mängd_bakpulver // 20
        mängd_bakpulver = mängd_bakpulver % 20
        mängd_bakpulver_msk = mängd_bakpulver // 3
        mängd_bakpulver = mängd_bakpulver % 3
        print(f"{mängd_bakpulver_dl} dl, {mängd_bakpulver_msk} msk, och {mängd_bakpulver} tsk bakpulver")
    elif mängd_bakpulver >= 3:
        mängd_bakpulver_msk = mängd_bakpulver // 3
        mängd_bakpulver = mängd_bakpulver % 3
        print(f"{mängd_bakpulver_msk} msk, och {mängd_bakpulver} tsk bakpulver")
    else:
        print(f"{mängd_bakpulver} tsk bakpulver")

    # vetemjöl räkning
    mängd_vetemjöl = vetemjöl * antal_sockerkakor
    if mängd_vetemjöl >= 10:
        mängd_vetemjöl_liter = mängd_vetemjöl // 10
        mängd_vetemjöl_dl = mängd_vetemjöl % 10
        print(f"{mängd_vetemjöl_liter} L och {mängd_vetemjöl_dl} dl vetemjöl")
    else:
        print(f"{mängd_vetemjöl} dl vetemjöl")

    # smör räkning
    mängd_smör = smör * antal_sockerkakor
    if mängd_smör >= 1000:
        mängd_smör_kilogram = mängd_smör // 1000
        mängd_smör = mängd_smör % 1000
        mängd_smör_hektogram = mängd_smör // 100
        mängd_smör = mängd_smör % 100
        print(f"{mängd_smör_kilogram} Kg, {mängd_smör_hektogram} Hg, och {mängd_smör} g smör")
    elif mängd_smör >= 100:
        mängd_smör_hektogram = mängd_smör // 100
        mängd_smör = mängd_smör % 100
        print(f"{mängd_smör_hektogram} Hg och {mängd_smör} g smör")
    else:
        print(f"{mängd_smör} g smör")

    # vatten räkning
    mängd_vatten = vatten * antal_sockerkakor
    if mängd_vatten >= 10:
        mängd_vatten_liter = mängd_vatten // 10
        mängd_vatten_dl = mängd_vatten % 10
        print(f"{mängd_vatten_liter} L och {mängd_vatten_dl} dl vatten")
    else:
        print(f"{mängd_vatten} dl vatten")

    # slut linje
    print("===========================================")
