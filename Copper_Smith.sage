def attack(high_m, n, c):
    R.<x> = PolynomialRing(Zmod(n), implementation='NTL')
    m = high_m + x
    M = m((m^3 - c).small_roots()[0])
    print(hex(int(M))[2:])
high_m=0x9876543210abcdef0000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
n=155266493936043103849855199987896813716831986416707080645036022909153373110367007140301635144950634879983289720164117794783088845393686109145443728632527874768524615377182297125716276153800765906014206797548230661764274997562670900115383324605843933035314110752560290540848152237316752573471110899212429555149
c=124929943232081828105808318993257526364596580021564021377503915670544445679836588765369503919311404328043203272693851622132258819278328852726005776082575583793735570095307898828254568015886630010269615546857335790791577865565021730890364239443651479580968112031521485174068731577348690810906553798608040451024
attack(high_m,n,c)