import click
from pyfiglet import Figlet
from extractDocx import *
from initiating import *
from signalepy import Signale
logger = Signale() 

f = Figlet(font='slant')

print(f.renderText('SearchMate'))
logger.info("Finding Please hold tight!!!", prefix="Debugger")
@click.command()
@click.option('--filename', '-f',
              type=click.Path(),
              required=True, help="Path to the file")

@click.option('--output_directory', '-o',default="./results.txt",
              help='Where to place the results')


def main(filename,output_directory):
    """
            audioConvertor is a command line tool that helps convert
            video files to audio file formats.\n
             example: python3 convert_parse.py -i input/file/path -o output/path
    """
    query = extractDocx(filename)
    initiating(query)


if __name__ == '__main__':
    main()