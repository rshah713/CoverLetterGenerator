import subprocess
import os

def convert_docx_to_pdf(docx_path, out_filename):
    if not os.path.isfile(docx_path):
        raise FileNotFoundError(f"File not found: {docx_path}")
    
    libreoffice_path = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    
    cmd = [
        libreoffice_path,
        "--headless",
        "--convert-to", "pdf",
        "--outdir", ".",
        docx_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
        pdf_name = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
        
        # Rename the output file to the specified filename
        if pdf_name != out_filename:
            os.rename(pdf_name, out_filename)
        
        print(f"==> PDF created at: {out_filename}")
        return out_filename
    except subprocess.CalledProcessError as e:
        print("==> ERROR: Conversion failed.")
        print(e)
        return None

if __name__ == "__main__":
    convert_docx_to_pdf("template.docx", "output.pdf")
