
import click
import requests
from datetime import datetime

import pprint

from listing_info import get_listing

pp = pprint.PrettyPrinter(width=120, compact=True)

@click.group(chain=True)
def cli():
    pass

@cli.command('print_today', short_help='Will print todays date')
def print_today():
    print(datetime.now())

# URL = 'https://www.pudim.com.br/'
# URL = 'https://www.daft.ie/'
URL = 'https://www.daft.ie/for-rent/apartment-bronze-ensuite-37-or-38-weeks-binary-hub-bonham-street-dublin-8/3501357/'

@cli.command('test', short_help='Will print todays date')
def test():
    get_listing(URL)

@cli.command('request', short_help='Will print todays date')
def request():
    resp = requests.get(URL)
    print(f"Status: {resp.status_code}")
    print(f"Text: {resp.text}")

    




if __name__ == '__main__':
    cli()