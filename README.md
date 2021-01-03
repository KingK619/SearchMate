
![license.MIT](https://img.shields.io/github/license/techyhoney/SearchMate) ![python3.x](https://img.shields.io/badge/python-3.x-brightgreen.svg) ![GitHub top language](https://img.shields.io/github/languages/top/techyhoney/SearchMate)
![GitHub release (latest by date)](https://img.shields.io/github/downloads/techyhoney/SearchMate/v1/total)
![GitHub contributors](https://img.shields.io/github/contributors/techyhoney/SearchMate)
<br/>
<br/>

<img src = "https://github.com/techyhoney/SearchMate/blob/master/search-mate.gif" />
<br/>

# SearchMate

SearchMate is CLI tool that helps in searching the equivalent content over the internet by taking reference of a document (.txt,.pdf,.docx) and list down the URL with their appropriate find scores.

## Features!

  - Fetchs links of web pages related to provided content.
  - Many of them aren't even ranked properly on google. So, it will help in exploring 
    some **rare treasures**!
  - Colorful CLI will help in better understanding of the things.
  - It can accept multiple formats of the file containing your content like `.txt`, `.docx`,
   `.pdf`(containg text and not text on images).
  - `Find Score` feartures lets you know how much of text in that link matchs yours.
  - Save results in a `.txt` file so you can refer it later.
  - You can store the output which is by default named `results.txt` in the path you wish, 
    
>**Note:** Make sure that terminal is opened in the same directory where the tool files are kept.

## Supported Python Versions

Python 3.6, 3.7, 3.8, and 3.9 are fully supported and tested. This library may work on later versions of 3, but we do not currently run tests against those versions.

## Unsupported Python Versions

Python < 3

## Prerequisites

After cloning this repository you will be requiring some packages to install. Ofcourse you will need 
[`python`](https://www.python.org/)  but there are few other dependencies that are require to use this application.  All of them 
are listed in  the [`requirements.txt`](https://github.com/techyhoney/SearchMate/blob/main/requirements.txt) file. You just have to follow the instructions below
in order to install them.

Open the terminal and execute the following command.
```sh
$  pip install requirements.txt
```
 After installing the dependencies , you are ready to use the tool!
 
## Usage

This tools itself holds an option which can show you its usage. Just execute the following
command in the terminal.
```sh
$ python main.py --help

Usage: main.py [OPTIONS]

  SearchMate is CLI tool that helps in searching the equivalent content over
  the internet by taking reference of a document(.txt,.pdf,.docx) and list
  down the URL with their appropriate find scores.

  Example: python main.py -f input/file/path -o output/path

  © SearchMate 2020

Options:
  -f, --filename PATH          Path to the file
  -o, --output_directory PATH  Where to place the results. Default = Current
                               Directory

  -d, --developer              About the Developers
  -q, --qna                    Frequently Asked Questions
  --help                       Show this message and exit.
  
  ```

<br>

```sh
$ python main.py -f file_name
```
After executing the above command, the links will be fetched and stored in the same
directory with the file name `results.txt`as well as displayed on the terminal.
For demo purpose, a file named `query.txt` is already there.

If you wish to store the results in a **specific path**, you'll need to execute the
following command instead.
```sh
$ python main.py -f file_name -o your_path
```
it will redirect the output to whatever path you've mentioned with the default file name.

There is also a faq section, you can check it out! 
```sh
$ python main.py --qna
```

## Development

We would love to get your suggestions and thoughts!
Please report any bug, if found!

Open your favorite Terminal and run these commands.
We'll be delighted to get your feedbacks!

**Free Software, Hell Yeah!**

## Thanks

A special thanks to `Karanveer Sidana` for
contributing to the project, who is quite literally the backbone of this project, that made this tool possible.
He has also provided valuable feedback and support during the development
of this app.

`Click <http://click.pocoo.org/>`_ is used for command line option parsing
and printing error messages.

Thanks to all the beta testers and contributors for your time and patience. :)

