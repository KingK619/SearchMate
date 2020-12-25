import click
from pyfiglet import Figlet,figlet_format
from extractDocx import *
from initiating import *
from output import *
from signalepy import Signale
logger = Signale() 

f = Figlet(font='slant')

print(f.renderText('SearchMate'))

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
    sorted_results = initiating(query)
    saveResults(sorted_results, output_directory)
    logger.complete("Results stored in " + output_directory)
    end = figlet_format('GoodBye!!',font = 'digital')
    print(end)

if __name__ == '__main__':
    main()