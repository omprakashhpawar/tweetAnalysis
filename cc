# query='trumph'
'''['trumph','namo','demonitization','cryptocurrency', 'bitcoin', 'bitcoins', 'ethereum', 'litecoin', 'bitcoinprice', 'blockchain', 'investment', 'investor', 'stockmarket', 'stocks', 'getrich', 	   'makemoney', 'makemoneyonline', 'mentorship', 'mentoring', 'xrp', 'bitfinex', 'altcoins', 'moneytalks', 'wealthy', 'wealthgenerators', 'bitcoinmining', 'ethereummining', 'freedomthinkers',  	  'decentralized', 'hofbrauhaus', 'prost', 'travel', 'travelblogger','travelgram', 'daytrading', 'investing', 'nyse', 'foodporn', 'cleveland', 'charlestonsc', 'germanbeer', 'finance', 'stock', 	   'financialtips', 'onlinemarketing', 'onlinebiz', 'forextrading', 'forex', 'entrepreneur', 'makeithappen', 'empower', 'onlinetrading', 'productivityhappy', 'dowjones', 'FF401k', 'foxandfriends',  	       'politicsasusual', 'mainstreammedia', 'buildthatwall', 'maga', 'trumptrain', 'liberaltears', 'safespace', 'Investing', 'Stocks', 'Liquidity', 'Bonds', 'Equity']'''






 # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
    plt.plot(t, ptweets, 'r--', t, ntweets, 'bs', t, ptweets-ntweets, 'g^')
    plt.show()
