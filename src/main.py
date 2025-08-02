import os
import argparse

from doc_to_pdf import convert_docx_to_pdf
from generate_cl import handler



def main():
    parser = argparse.ArgumentParser(description="Cover Letter Generator")
    parser.add_argument('-c', '--company', required=True, help='Company name')
    parser.add_argument('-t', '--team', required=False, help='Team name (optional)')
    parser.add_argument('-p', '--template', required=False, help='.docx template path (optional)')
    parser.add_argument('-n', '--name', required=False, help='Name (optional)')
    args = parser.parse_args()

    company_name = args.company
    team_name = args.team if args.team else "Software Engineering"
    name = args.name if args.name else "Rohan Shah"
    template_path = args.template if args.template else os.path.expanduser("~/git/CoverLetterGenerator/src/template.docx")

    handler(template_path, company_name, team_name)
    convert_docx_to_pdf("temp_filled.docx", f'{name} - {company_name} Cover Letter.pdf')

    if os.path.exists("temp_filled.docx"):
        os.remove("temp_filled.docx")


if __name__ == "__main__":
    main()
