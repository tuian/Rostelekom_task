import asyncio
import csv
import os
import re
import subprocess
import requests
import json
from APTnotes_async_download_python35 import download_all_reports

HASHES = {
    'sha1': re.compile(r'(\b[0-9a-f]{40}\b)'),
    'md5': re.compile(r'(\b[0-9a-f]{32}\b)')
}

download_path = "download_pdfs"


def convert_pdf_to_txt(path):
    subprocess.call(['pdftotext', path, 'output'])
    with open('output', 'r') as fp:
        text = fp.readlines()
    return ''.join(text)


def get_iocs(text):
    iocs = {k: [] for k in HASHES.keys()}
    try:
        for hash_name, regex in HASHES.items():
            result = regex.finditer(text)
            if result:
                iocs[hash_name] = []
                for match in result:
                    iocs[hash_name].append(match.group())
    except Exception as e:
        print(e)
    return iocs


if __name__ == '__main__':
    github_url = "https://raw.githubusercontent.com/aptnotes/" \
                 "data/master/APTnotes.json"
    APTnotes = requests.get(github_url)
    APT_reports = json.loads(APTnotes.text)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_reports(loop, APT_reports, download_path))
    APT_reports = csv.DictReader(open('APTnotes.csv'))
    fieldnames = ['Filename', 'Title', 'Source', 'Link', 'SHA-1',
                  'Type', 'Hash', 'Date', 'Year']
    NEW_APT_reports = csv.DictWriter(open('../get_server/app/uploads/NEW_APTnotes.csv', 'w'),
                                     fieldnames=fieldnames)
    NEW_APT_reports.writeheader()
    for row in APT_reports:
        filename = row['Filename']
        year = row['Year']
        path = os.path.join(download_path ,year, filename)
        text = convert_pdf_to_txt(path + '.pdf').lower()
        iocs = get_iocs(text)
        buf_row = {k: v for k, v in row.items()}
        for hash_name, hashes in iocs.items():
            for hash in hashes:
                buf_row.update({'Type': hash_name, 'Hash': hash})
                NEW_APT_reports.writerow(buf_row)
