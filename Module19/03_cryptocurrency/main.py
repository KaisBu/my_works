data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

for key in data.keys():
    if key == 'ETH':
        print('\n{key}:'.format(key=key))

        for keys in data[key]:
            print('{key}: {value}'.format(key=keys, value=data.get(key).get(keys)))

    elif key == 'tokens':
        print('\n{key}:'.format(key=key))

        for elem in data[key]:
            for keys in elem.keys():
                if keys == 'fst_token_info' or keys == 'sec_token_info':
                    print('\n{key}:'.format(key=keys))
                    for part in elem[keys].keys():
                        print('{key}: {value}'.format(key=part,
                                                      value=elem[keys].get(part)))
                else:
                    print('{key}: {value}'.format(key=keys,
                                                  value=elem.get(keys)))

    else:
        print('\n{key}: {value}'.format(key=key, value=data.get(key)))

data['ETH']['total_diff'] = 100
data['tokens'][0]['fst_token_info']['name'] = 'doge'
data['ETH']['total_out'] += data['tokens'][0]['total_out'] + \
                            data['tokens'][1]['total_out']
data['tokens'][0].pop('total_out')
data['tokens'][1].pop('total_out')
data['tokens'][1]['sec_token_info']['total_price'] = \
    data['tokens'][1]['sec_token_info'].pop('price')

