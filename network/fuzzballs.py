from clove.network.bitcoin import Bitcoin


class FuzzBalls(Bitcoin):
    """
    Class with all the necessary FuzzBalls (FUZZ) network information based on
    https://bitbucket.org/aminerminer/fuzzcoin/src/2ad64dc272f4984a24f1b0e69ff9e5c4d6dcaa60/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'fuzzballs'
    symbols = ('FUZZ', )
    seeds = ('167.114.13.141')
    port = 62126


class FuzzBallsTestNet(FuzzBalls):
    """
    Class with all the necessary FuzzBalls (FUZZ) testing network information based on
    https://bitbucket.org/aminerminer/fuzzcoin/src/2ad64dc272f4984a24f1b0e69ff9e5c4d6dcaa60/src/net.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-fuzzballs'
    seeds = ('167.114.13.141')
    port = 72126
