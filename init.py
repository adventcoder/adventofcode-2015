import os
from datetime import *
import requests
import click

year = 2015
server_tz = timezone(timedelta(hours=-5), 'EST')

def get_input_path(day):
    return f'inputs/day{day}.txt'

@click.command()
@click.option('--session', envvar='ADVENTOFCODE_SESSION', required=True)
@click.option('--clean', is_flag=True)
@click.option('--day', type=int)
def main(session, clean, day):
    if day is None:
        day = last_available_day()
    for day in range(1, day + 1):
        if clean:
            delete_input(day)
        download_input(day, session)

def last_available_day():
    server_time = datetime.now(server_tz)
    if server_time.year < year or (server_time.year == year and server_time.month < 12):
        return 0
    if server_time.year == year and server_time.month == 12 and server_time.day <= 25:
        return server_time.day
    return 25

def delete_input(day):
    path = get_input_path(day)
    if not os.path.exists(path):
        click.echo(f'Input not yet downloaded for day {day}')
    else:
        click.echo(f'Deleting input for day {day}')
        os.remove(path)

def download_input(day, session):
    path = get_input_path(day)
    if os.path.exists(path):
        click.echo(f'Already downloaded input for day {day}')
    else:
        click.echo(f'Downloading input for day {day}')
        res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={ 'session': session })
        res.raise_for_status()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'x') as file:
            file.write(res.text)

if __name__ == '__main__':
    main()
