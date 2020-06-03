from quatro import log, configuration as c
from subprocess import check_output
import os


def outstanding_pos_ninja(po_number=None):
    report_path = c.config.parent_dir + "\\files\\crystal reports\\GABON001 - Bon d'achat - Quatro Bilingual.rpt"
    output_name = f'\\{po_number}.pdf'
    output_path = c.config.pdf_dir + output_name

    command = f'"{c.config.ninja}" -D QuatroAir -U SIGM -F "{report_path}" -O "{output_path}" ' \
              f'-a "NoFormat:0" ' \
              f'-a NoBonAchat:({po_number},{po_number})"'

    log(f'Sending following command to shell : {command} \n')
    check_output(command, shell=True).decode()
    report_pdf = {'file': output_path, 'name': output_name}

    return report_pdf


def delete_pdfs():
    for file in os.listdir(c.config.pdf_dir):
        file_path = c.config.pdf_dir + f'\\{file}'
        os.remove(file_path)
        log(f'Deleted {file_path} \n')


if __name__ == "__main__":
    outstanding_pos_ninja()
    delete_pdfs()
