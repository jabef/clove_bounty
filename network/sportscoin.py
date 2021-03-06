from clove.network.bitcoin import Bitcoin


class SportsCoin(Bitcoin):
    """
    Class with all the necessary SportsCoin network information based on
    https://github.com/thesportscoin/sport-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'sportscoin'
    symbols = ('SPORT', )
    seeds = ("63.142.255.39")
    port = 42986


# Has no testnet