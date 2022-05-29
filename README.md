# Automatic massloading of accounts on [Lolz Market](https://lolz.guru/market)

# Installing
- Setup [Python](https://www.python.org/downloads/release/python-3912/)

  *Note*: Add to PATH checkbox is up
### Go to cmd/terminal and:
- Clone this repository `git clone https://github.com/choppaDev/automassload_lolzmarket.git` or another way
- Go to the repository directory `cd "your path"`

  *Example*: `cd "/home/kali/Desktop/automassload_lolzmarket/"`
- Install additional libraries `pip install -r /path/to/requirements.txt`
### Installing Chrome + chromedriver:
- You can do it yourself for a specific OS

*Note*: the driver version must match the browser version.
____
# Setting
### Go to cfg.env and enter your values
```
login = *your login on Lolz*
password = *your password on Lolz*
accounts = *Discord/Instagram/VK*
accounts_origin = *Origin of accounts, check available in massload page, Example: Autoregs*
name_ru = *Name of article on RU language*
name_en = *Name of article on EN language*
price = *Price of article*
description = *Description of article*
info_for_buyer = *Afterpurchase message*
discount_value = *Can buyer to ask discount? 0 if can't*
path_to_accs = *Your path to accs.txt*
path_to_chromedriver = *Your path to chromedriver*
```
____
# Launch
`python main.py`
