from doc_to_pdf import convert_docx_to_pdf
from generate_cl import handler

import argparse

def main():
    parser = argparse.ArgumentParser(description="Cover Letter Generator")
    parser.add_argument('-c', '--company', required=True, help='Company name')
    parser.add_argument('-t', '--team', required=False, help='Team name (optional)')
    args = parser.parse_args()

    company_name = args.company
    team_name = args.team if args.team else "Software Engineering"

    handler(company_name, team_name)
    convert_docx_to_pdf("temp_filled.docx", f'Rohan Shah - {company_name} Cover Letter.pdf')


if __name__ == "__main__":
    main()
