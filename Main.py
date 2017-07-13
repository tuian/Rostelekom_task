import re
import json
import requests
import os
import asyncio
from APTnotes_async_download_python35 import download_all_reports
import subprocess

HASHES = {
    'sha1': re.compile('([0-9a-f]{40})'),
    'md5': re.compile('([0-9a-f]{32})')
}


def convert_pdf_to_txt(path):
    subprocess.call(['pdftotext', path, 'output'])
    with open('output','r') as fp:
        text = fp.readlines()
    return ''.join(text)


def get_iocs(text):
    iocs = {k: [] for k in HASHES.keys()}
    try:
        for hash_name, regex in HASHES.items():
            result = regex.search(text)
            if result:
                for hash in result.groups():
                    iocs[hash_name] = hash
    except Exception as e:
        print(path)
        print(e)
    return iocs


if __name__ == '__main__':
    github_url = "https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.json"
    APTnotes = requests.get(github_url)
    APT_reports = json.loads(APTnotes.text)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_reports(loop, APT_reports))
    for i in APT_reports:
        filename = i['Filename']
        year = i['Year']
        path = os.path.join(year, filename + '.pdf')
        text = convert_pdf_to_txt(path).lower()
        print(filename)
        print(get_iocs(text))

