from clove.network.bitcoin import Bitcoin


class  LeafCoin(Bitcoin):
    """
    Class with all the necessary  LeafCoin (LEAF) network information based on
    https://github.com/leafcoin/leafcoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'leafcoin'
    symbols = ('LEAF', )
    seeds =  ('seed.leafco.in', 'seed2.leafco.in', 'seed3.leafco.in',
			'seed4.leafco.in', 'seed5.leafco.in', 'leafcoin.mercuriusgids.nl')
    port = 22813


# no testnet