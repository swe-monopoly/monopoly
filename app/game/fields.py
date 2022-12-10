CITY = 'CITY'
START = 'START'
TRAIN = 'TRAIN'
POWERPLANT = 'POWERPLANT'
SECRET = 'SECRET'
PRISON = 'PRISON'
GOTO = "GOTO"
PARKING = 'PARKING'
FINE = 'FINE'

FIELDS = [
    {
        'id': 0,
        'label': 'START',
        'type': START
    }, {
        'id': 1,
        'label': 'PACIFIC AVENUE',
        'type': CITY,
        'price': 120,
        'pricing': {
            '0': 10, '1': 40, '2': 120, '3': 360, '4': 640, 'h': 900
        },
        'build_price': 100
    }, {
        'id': 2,
        'label': 'XX PASS XX',
        'type': SECRET
    }, {
        'id': 3,
        'label': 'NORTH CAROLINA AVENUE',
        'type': CITY,
        'price': 120,
        'pricing': {
            '0': 10, '1': 40, '2': 120, '3': 360, '4': 640, 'h': 900
        },
        'build_price': 100
    }, {
        'id': 4,
        'label': 'Income Tax',
        'type': FINE
    }, {
        'id': 5,
        'label': 'KING\'S CROSS STATION',
        'type': TRAIN
    }, {
        'id': 6,
        'label': 'PENNSYLVANIA AVENUE',
        'type': CITY,
        'price': 200,
        'pricing': {
            '0': 15, '1': 60, '2': 180, '3': 540, '4': 800, 'h': 1100
        },
        'build_price': 100
    }, {
        'id': 7,
        'label': 'XX PASS XX',
        'type': SECRET
    }, {
        'id': 8,
        'label': 'PARK PLACE',
        'type': CITY,
        'price': 200,
        'pricing': {
            '0': 15, '1': 60, '2': 180, '3': 540, '4': 800, 'h': 1100
        },
        'build_price': 100
    }, {
        'id': 9,
        'label': 'BOARDWALK',
        'type': CITY,
        'price': 240,
        'pricing': {
            '0': 20, '1': 80, '2': 200, '3': 600, '4': 900, 'h': 1200
        },
        'build_price': 100
    }, {
        'id': 10,
        'label': 'IN JAIL',
        'type': PRISON
    }, {
        'id': 11,
        'label': 'MEDITERRANEAN AVENUE',
        'type': CITY,
        'price': 280,
        'pricing': {
            '0': 20, '1': 100, '2': 300, '3': 900, '4': 1250, 'h': 1500
        },
        'build_price': 200
    }, {
        'id': 12,
        'label': 'ELECTRIC COMPANY',
        'type': POWERPLANT
    }, {
        'id': 13,
        'label': 'BALTIC AVENUE',
        'type': CITY,
        'price': 280,
        'pricing': {
            '0': 20, '1': 100, '2': 300, '3': 900, '4': 1250, 'h': 1500
        },
        'build_price': 200
    }, {
        'id': 14,
        'label': 'FLORIDA CITY',
        'type': CITY,
        'price': 320,
        'pricing': {
            '0': 25, '1': 120, '2': 360, '3': 1000, '4': 1400, 'h': 1800
        },
        'build_price': 200
    }, {
        'id': 15,
        'label': 'READING RAILROAD',
        'type': TRAIN
    }, {
        'id': 16,
        'label': 'CONNECTICUT AVENUE',
        'type': CITY,
        'price': 360,
        'pricing': {
            '0': 30, '1': 140, '2': 400, '3': 1100, '4': 1500, 'h': 1900
        },
        'build_price': 200
    }, {
        'id': 17,
        'label': 'XX PASS XX',
        'type': SECRET
    }, {
        'id': 18,
        'label': 'ORIENTAL AVENUE',
        'type': CITY,
        'price': 360,
        'pricing': {
            '0': 30, '1': 140, '2': 400, '3': 1100, '4': 1500, 'h': 1900
        },
        'build_price': 200
    }, {
        'id': 19,
        'label': 'VERMONT AVENUE',
        'type': CITY,
        'price': 400,
        'pricing': {
            '0': 35, '1': 160, '2': 440, '3': 1200, '4': 1600, 'h': 2000
        },
        'build_price': 200
    }, {
        'id': 20,
        'label': 'PARKING',
        'type': PARKING
    }, {
        'id': 21,
        'label': 'MARVIN GARDENS',
        'type': CITY,
        'price': 440,
        'pricing': {
            '0': 35, '1': 180, '2': 500, '3': 1400, '4': 1750, 'h': 2100
        },
        'build_price': 300
    }, {
        'id': 22,
        'label': 'XX PASS XX',
        'type': SECRET
    }, {
        'id': 23,
        'label': 'VENTOR AVENUE',
        'type': CITY,
        'price': 440,
        'pricing': {
            '0': 35, '1': 180, '2': 500, '3': 1400, '4': 1750, 'h': 2100
        },
        'build_price': 300
    }, {
        'id': 24,
        'label': 'ATLANTIC AVENUE',
        'type': CITY,
        'price': 480,
        'pricing': {
            '0': 40, '1': 200, '2': 600, '3': 1500, '4': 1850, 'h': 2200
        },
        'build_price': 300
    }, {
        'id': 25,
        'label': 'ILLINOIS AVENUE',
        'type': TRAIN
    }, {
        'id': 26,
        'label': 'TEXAS',
        'type': CITY,
        'price': 520,
        'pricing': {
            '0': 45, '1': 220, '2': 660, '3': 1600, '4': 1950, 'h': 2300
        },
        'build_price': 300
    }, {
        'id': 27,
        'label': 'INDIANA AVENUE',
        'type': CITY,
        'price': 520,
        'pricing': {
            '0': 45, '1': 220, '2': 660, '3': 1600, '4': 1950, 'h': 2300
        },
        'build_price': 300
    }, {
        'id': 28,
        'label': 'KENTUCKY AVENUE',
        'type': POWERPLANT
    }, {
        'id': 29,
        'label': 'NEWYORK AVENUE',
        'type': CITY,
        'price': 560,
        'pricing': {
            '0': 50, '1': 240, '2': 720, '3': 1700, '4': 2050, 'h': 2400
        },
        'build_price': 300
    }, {
        'id': 30,
        'label': 'TENNESSE AVENUE',
        'type': GOTO
    }, {
        'id': 31,
        'label': 'ST.JAMES PLACE',
        'type': CITY,
        'price': 600,
        'pricing': {
            '0': 55, '1': 260, '2': 780, '3': 1900, '4': 2200, 'h': 2550
        },
        'build_price': 400
    }, {
        'id': 32,
        'label': 'VIRGINIA AVENUE',
        'type': CITY,
        'price': 600,
        'pricing': {
            '0': 55, '1': 260, '2': 780, '3': 1900, '4': 2200, 'h': 2550
        },
        'build_price': 400
    }, {
        'id': 33,
        'label': 'XX PASS XX',
        'type': SECRET
    }, {
        'id': 34,
        'label': 'STATES AVENUE',
        'type': CITY,
        'price': 640,
        'pricing': {
            '0': 60, '1': 300, '2': 900, '3': 2000, '4': 2400, 'h': 2800
        },
        'build_price': 400
    }, {
        'id': 35,
        'label': 'ST.CHARLES PLACE',
        'type': TRAIN
    }, {
        'id': 36,
        'label': 'XX PASS XX',
        'type': SECRET
    }, {
        'id': 37,
        'label': 'FAIRFAX COUNTY',
        'type': CITY,
        'price': 700,
        'pricing': {
            '0': 70, '1': 350, '2': 1000, '3': 2200, '4': 2600, 'h': 3000
        },
        'build_price': 400
    }, {
        'id': 38,
        'label': 'HERNDON',
        'type': FINE
    }, {
        'id': 39,
        'label': 'ASHBURN',
        'type': CITY,
        'price': 800,
        'pricing': {
            '0': 100, '1': 400, '2': 1200, '3': 2800, '4': 3400, 'h': 4000
        },
        'build_price': 400
    },
]