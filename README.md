# Vanozy

Vanozy is a vanity address miner for the Nyzo crypto currency.

It looks for a given string in the nyzoString encoded public identifier.

## What are Nyzo Strings?

See https://github.com/AngainorDev/NyzoStrings

Nyzo strings are safe - types and checksumed - strings that represent Nyzo objects.

There are Nyzo strings for Private seed, Public identifier (addresses), transactions...  
Nyzo strings are the future proof way to encode these objects, and we can expect the upcoming tools to make use of these strings instead of the legacy raw hex format.


## Requirements

- python 3.6+
- click module, `pip3 install click` or use `pip3 install -r requirements.txt`


## How to use

Run with no argument to get help:

`python3 Vanozy.py`

```
Usage: Vanozy.py [OPTIONS] COMMAND [ARGS]...

Options:
  -c, --case               Do case sensitive lookups (default False)
  -p, --processes INTEGER  Processes to start (default 4)
  -m, --max INTEGER        Max matches per process (default 10)
  --help                   Show this message and exit.

Commands:
  find
  version
```

> if you `chmod +x Vanozy`, you can run it straight with `./Vanozy...`

For instance, to lookup addresses with "egg" string, case insensitive, default params:  
`python3 Vanozy.py find egg`

On a 32 cores CPU:  
`python3 Vanozy.py -p 32 find egg`

Vanozy does spit out one line per matching address,  
nyzo_id_string private_seed_as_hex_with_dashes

Example output (do **not** use these addresses ever irl, since their seeds are now public)

Command was `python3 Vanozy.py -p 1 -m 5 -c find EGG`  
That is One process, stop after 5 matches, case sensitive, look for 'EGG'

```
Looking for 'EGG' Case sensitive with 1 processes
id__88RPxdoK9Koq-kBtRnDTCmMpEGG1H-71Y15jmDKwA2nVPtInY5Ud 8cf180d5ed26d5d9-f1491ccd69b5955b-d89e9a41abc1c1e8-1153566b5f8c25b7
id__8d9nDQKSWyPLkeKNrq3-GELNrfFt6Vv25KTxTB3vEGGo6iK4HTQn d2569b2b74e21c6e-50eb706990fca67b-b068fa1c1b778216-dd60d640de9e9a57
id__87DiinXvKj5R8968hI7jGyiVc8biecsD5V8~ktqVEGG-JZ2nbw~t 7992496e5eb53173-20918846b1d3a614-b73082d238c6e617-723e51c6779e9a7c
id__8d6jkkMpv2_nZjTxfdh7pEGGHno0Af2Gt~8sdmn2J.3KyZFf8nvH d193514bd8782fd6-ed3d603cd447627a-69a965c08cf0a973-e21b355582b3d0ed
id__8e2aHqp1u4Nm1kAtF8BRuKNeSuWzGEGG91~ILh1v~uCqd90epINJ e08aa99601744c15-0548dca0893376dc-0ed1de22a67a6924-1fabb9105ef9d959
id__89Vx3P4cQfEGG~uRLa_Bru6Srq_RErQMbXfzRpKQ-Yt~_ora.SnB 9de00f110cc8f9e9-a7e773b8afe469d1-b4699ff39dacaf2f-93e2cd8b72f3a73e
```

## Notes 

Ships with a frozen copy of nyzostring - python port - supporting only Public Identifiers nyzo Strings.  
That will be converted later on to use a pypi module.

## Tip Jar

Show your appreciation, send a few coffees or pizzas to the dev:
`abd7fede35a84b10-8a36e6dc361d9b32-ca84d149f6eb85b4-a4e63015278d4c9f`


## Changelog

- 0.2: format improvement, doc
- 0.1: First test



 
