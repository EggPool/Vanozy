#!/usr/bin/env python3
"""
Generate vanity Nyzo id__ strings

EggdraSyl - Oct. 2019.
"""

import click
import sys
# from os import urandom
from secrets import token_hex
from multiprocessing import Process
from nyzostrings.nyzostringpublicidentifier import NyzoStringPublicIdentifier
from nyzostrings.nyzostringencoder import NyzoStringEncoder


ALPHABET = "0123456789abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ-.~_"


__version__ = "0.2"


def split_by_len(item, maxlen):
    return (item[ind:ind+maxlen] for ind in range(0, len(item), maxlen))


def bytes_as_string_with_dashes(hexa: str) -> str:
    return '-'.join(split_by_len(hexa, 16))


def find_it(string: str, ctx):
    found = 0
    while True:
        # pk = urandom(32).hex()
        pk = token_hex(32)  # +50% time, but supposed to be cryptographically secure
        nyzo_string = NyzoStringPublicIdentifier.from_hex(pk)
        address = NyzoStringEncoder.encode(nyzo_string)
        if not ctx.obj['case']:
            address = address.lower()
        if string in address:
            print(address, bytes_as_string_with_dashes(pk))
            found += 1
            if found > ctx.obj['max']:
                return


@click.group()
@click.option('--case', '-c',  is_flag=True, default=False, help='Do case sensitive lookups (default False)')
@click.option('--processes', '-p', default=4, help='Processes to start (default 4)')
@click.option('--max', '-m', default=10, help='Max matches per process (default 10)')
@click.pass_context
def cli(ctx, case, processes, max):
    ctx.obj['case'] = case
    ctx.obj['processes'] = processes
    ctx.obj['max'] = max


@cli.command()
@click.pass_context
@click.argument('string', type=str)
def find(ctx, string: str):
    case = "Case sensitive"
    if not ctx.obj['case']:
        string = string.lower()
        case = "Case InsEnsITivE"
    print("Looking for '{}' {} with {} processes".format(string, case, ctx.obj['processes']))
    # Check charset is ok ? not easy with case insensitive...
    processes = []
    for i in range(ctx.obj['processes']):
        p = Process(target=find_it, args=(string, ctx))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


@cli.command()
@click.pass_context
def version(ctx):
    print("Vanozy version {}".format(__version__))


if __name__ == "__main__":
    cli(obj={})


