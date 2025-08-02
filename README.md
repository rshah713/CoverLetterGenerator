# CoverLetterGenerator
Built for myself because I'm tired of writing custom cover letters and LLM generated ones are trash.

Base template (not GPT'd!) is provided. Tool is used to customize company name, team, and date and output pdf. 

Tested only on my system (macOS), no guarantees this will work for you!

-------
## Installation

```bash
pip install -r requirements.txt # for customizing docx template
brew install libreoffice # for pdf export
```

-------
## Usage
```bash
usage: main.py [-h] -c COMPANY [-t TEAM] [-p TEMPLATE] [-n NAME]

Cover Letter Generator

options:
  -h, --help            show this help message and exit
  -c, --company COMPANY
                        Company name
  -t, --team TEAM       Team name (optional)
  -p, --template TEMPLATE
                        .docx template path (optional)
  -n, --name NAME       Full name (optional)
```

Simple Example:
```bash
$ python3 ~/Documents/CoverLetterGenerator/src/main.py -c Google
==> PDF created at: ~/Downloads/Rohan Shah - Google Cover Letter.pdf

$ python3 ~/Documents/CoverLetterGenerator/src/main.py -c "Capital One" -t "Enterprise Services"
==> PDF created at: ~/Downloads/Rohan Shah - Capital One Cover Letter.pdf
```
-------
## Alias
For easier usage, you can `alias` the absolute path of the tool to a friendly command.

```bash
$ alias covergen='python3 ~/Documents/CoverLetterGenerator/src/main.py'

$ covergen -c Apple
usage: main.py [-h] -c COMPANY [-t TEAM] [-p TEMPLATE]

Cover Letter Generator

options:
  -h, --help            show this help message and exit
  -c, --company COMPANY
                        Company name
  -t, --team TEAM       Team name (optional)
  -p, --template TEMPLATE
                        .docx template path (optional)
```

Recall this is only session dependent, add to `.bashrc or .zprofile` to save the alias.

-------
## Customization
You'll likely need to customize the email, github link, university, etc. 

It's best if you download the `template.docx` provided, edit the values and save it to the same directory. I didn't feel like providing a programmatic way to update this b/c it should stay static for all the cover letters you generate. 

-------
## Possible Issues

None of the following solutions are tested as this program was built for personal use. 

> `libreoffice` PATH is incorrect.

Use `which libreoffice` to locate the download path and replace it in `convert_docx_to_pdf`


> `template.docx` is not found

Utilize `main.py -p` to pass the absolute path of the template OR to add your own template. 
