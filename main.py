# -*- coding: utf-8 -*-
# Master script for the SearchMate
# Coded by: Hiten Goyal & Karanvver Sidana

import click
from modules import *
from extractDocx import *
from __init__ import *
from output import *

# logs stats of SearchMate on console
logger = Signale() 

f = Figlet(font='slant')
print((colored(figlet_format("SearchMate"), color="yellow")))

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
            the internet by taking reference of a document(.txt,.pdf,.docx) and list down the URL with their appropriate find scores.\n
            Example: python main.py -f input/file/path -o output/path

            © SearchMate 2020
    """
    if qna:
      click.echo(
    """
  \033[96mQ1. What is Find Score?\n
  Find Score is being referred to as an algorithm that
  is calculating the similarity scores for the provided
  document over the internet.

  \033[96mQ2. What Packages are required to run this tool?\n
  We have included a requirements.txt file which has all 
  the required modules. Just run\033[93m pip install requirements.txt

  \033[96mQ3. How accurate the tool is?
  The tool searches web based on the document you provide to
  give results similar to the query. Accuracy of tool is around 95%. 
    """
          )
      exit()

    if developer:
        click.echo(
    """  1. Hiten Goyal (Founder)

  2. Karanveer Sidana (Co Founder)
    """
          )
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
