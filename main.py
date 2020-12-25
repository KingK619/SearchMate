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

@click.option('--output_directory', '-o',default="./",
              type=click.Path(), help='Where to place the results. Default = Current Directory')


def main(filename,output_directory):
    """
            SearchMate is CLI tool that helps in searching the equivalent content over
            the internet by taking refernce of a document(.txt,.pdf,.docx) and list down the URL to them with their appropriate find scores.\n
            Example: python main.py -f input/file/path -o output/path

            © SearchMate 2020
    """
    query = extractDocx(filename)
    sorted_results = initiating(query)
    saveResults(sorted_results, output_directory)
    logger.complete("Results stored in " + output_directory)
    end = figlet_format('GoodBye!!',font = 'digital')
    print(end)

if __name__ == '__main__':
    main()