
from clove.network.bitcoin import Bitcoin


class Bitz(Bitcoin):
    """
    Class with all the necessary BITZ network information based on
    http://www.github.com/MOJOv3/mojocoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitz'
    symbols = ('BITZ', )
    seeds = ('mojonode01.mojocoin.org', 'mojonode02.mojocoin.org', 'mojonode03.mojocoin.org', 'mojonode04.mojocoin.org', 'mojonode05.mojocoin.org', 'mojonode06.mojocoin.org', 'mojonode07.mojocoin.org', 'mojonode08.mojocoin.org', 'mojonode09.mojocoin.org')
    port = 9495


class BitzTestNet(Bitz):
    """
    Class with all the necessary BITZ testing network information based on
    http://www.github.com/MOJOv3/mojocoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitz'
    seeds = ()
    port = 19495
