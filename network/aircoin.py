from clove.network.bitcoin import Bitcoin


class AIRcoin(Bitcoin):
    """
    Class with all the necessary AIRcoin network information based on
    https://github.com/TeamAIRcoin/AIRcoin/blob/master/src/net.cpp#L17
    (date of access: 02/13/2018)
    """
    name = 'aircoin'
    symbols = ('AIR', )
    seeds =  ("dnsseed.aircointools.org",
              "aircointools.com",
              "dnsseed.ltc.xurious.com",
              "dnsseed.koin-project.com",
              "dnsseed.weminemnc.com")	
    port = 1631
	
   
class AIRcoinTestNet(AIRcoin):
    """
    Class with all the necessary AIRcoin testing network information based on
    https://github.com/TeamAIRcoin/AIRcoin/blob/master/src/net.cpp#L17
    (date of access: 02/13/2018)
    """
    name = 'test-aircoin'
    seeds = ("testnet-seed.AIRcointools.com",
             "testnet-seed.weminemnc.com")
    port = 1632              
	
	



