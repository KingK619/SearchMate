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
              help="Path to the file")

@click.option('--output_directory', '-o',default="./",
              type=click.Path(), help='Where to place the results. Default = Current Directory')

@click.option('--developer','-d', is_flag=True,help="About the Developers")
@click.option('--qna','-q', is_flag=True,help="Frequently Asked Questions")

   

def main(filename,output_directory,developer,qna):
    """
            SearchMate is CLI tool that helps in searching the equivalent content over
            the internet by taking refernce of a document(.txt,.pdf,.docx) and list down the URL to them with their appropriate find scores.\n
            Example: python main.py -f input/file/path -o output/path

            © SearchMate 2020
    """
    if qna:
        click.echo("Q1. What is Find Score?")
        exit()

    if developer:
        click.echo("Some shit About the developers...")
        exit()
    if(filename):
        query = extractDocx(filename)
        sorted_results = initiating(query)
        saveResults(sorted_results, output_directory)
        logger.complete("Results stored in " + output_directory +"results.txt")
        end = figlet_format('GoodBye!!',font = 'digital')
        print(end)
    else:
        logger.error("Please Input a document!!!!")
    


if __name__ == '__main__':
    main()
