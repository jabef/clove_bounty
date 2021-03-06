from clove.network.bitcoin import Bitcoin


class YbCoin(Bitcoin):
    """
    Class with all the necessary YbCoin network information based on
    https://github.com/ybcoin/ybcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'ybcoin'
    symbols = ('YBC', )
    seeds = ("seeds.ybcoin.com",
             "seed1.ybcoin.org",
             "seed2.ybcoin.org",
             "tnseeds.ybcoin.com")
    port = 7337
	
