
import click
from datetime import datetime

import pprint

from here import get_address

pp = pprint.PrettyPrinter(width=120, compact=True)

@click.group(chain=True)
def cli():
    pass

@cli.command('print_today', short_help='Will print todays date')
def print_today():
    print(datetime.now())


@cli.command('get_coordinates', short_help='Will print todays date')
@click.argument('address')
def get_coordinates(address):
    pp.pprint(get_address(address))



if __name__ == '__main__':
    cli()