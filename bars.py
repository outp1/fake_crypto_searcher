from progress.bar import Bar
import random

text = '''torrequest
pysocks
bitcash
bip32utils==0.3.post4
colored
notify-py
pysocks
ctypes
urllib3==1.26.4
idna==2.10
ecdsa==0.16.1
certifi==2020.12.5
requests[security]
fake_useragent
selenium
torpy
bs4
lxml
base58==2.1.0
certifi==2021.5.30
requests==2.25.1
urllib3==1.26.6
bitcash'''

#result = 'bars = ['
#for line in text.split('\n'):
#    result += f'Bar("{line}", max={random.randint(4, 100)}),\n'
#result += ']'
#
#print(result)

bars = [Bar("torrequest", max=18),
Bar("pysocks", max=91),
Bar("bitcash", max=9),
Bar("bip32utils==0.3.post4", max=94),
Bar("colored", max=62),
Bar("notify-py", max=50),
Bar("pysocks", max=25),
Bar("ctypes", max=71),
Bar("urllib3==1.26.4", max=88),
Bar("idna==2.10", max=40),
Bar("ecdsa==0.16.1", max=49),
Bar("certifi==2020.12.5", max=27),
Bar("requests[security]", max=32),
Bar("fake_useragent", max=59),
Bar("selenium", max=18),
Bar("torpy", max=82),
Bar("bs4", max=68),
Bar("lxml", max=32),
Bar("base58==2.1.0", max=65),
Bar("certifi==2021.5.30", max=87),
Bar("requests==2.25.1", max=97),
Bar("urllib3==1.26.6", max=14),
Bar("bitcash", max=57),
]
