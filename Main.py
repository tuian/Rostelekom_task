import asyncio
import csv
import os
import re
import subprocess

from APTnotes_async_download_python35 import download_all_reports

HASHES = {
    'sha1': re.compile('([0-9a-f]{40})'),
    'md5': re.compile('([0-9a-f]{32})')
}


def convert_pdf_to_txt(path):
    subprocess.call(['pdftotext', path, 'output'])
    file = open('output', 'r')
    text = file.readlines()
    return ''.join(text)

def get_iocs(text):
    iocs = {k: [] for k in HASHES.keys()}
    try:
        for hash_name, regex in HASHES.items():
            result = regex.search(text)
            if result:
                iocs[hash_name] = []
                for hash in result.groups():
                    iocs[hash_name].append(hash)
    except Exception as e:
        print(path)
        print(e)
    return iocs


if __name__ == '__main__':
    # github_url = "https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.json"
    # APTnotes = requests.get(github_url)
    # APT_reports = json.loads(APTnotes.text)
    APT_reports = csv.DictReader(open('APTnotes.csv'))
    fieldnames = ['Filename', 'Title', 'Source', 'Link', 'SHA-1', 'MD5', 'SHA1', 'Date', 'Year']
    NEW_APT_reports = csv.DictWriter(open('NEW_APTnotes.csv', 'w'), fieldnames=fieldnames)
    NEW_APT_reports.writeheader()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_reports(loop, APT_reports))
    for i in APT_reports:
        filename = i['Filename']
        year = i['Year']
        path = os.path.join(year, filename)
        text = convert_pdf_to_txt(path).lower()
        array = get_iocs(text)
        if len(array['sha1']) == 0 or len(array['md5']) == 0:
            for j in array['sha1']:
                NEW_APT_reports.writerow({'Filename': i['Filename'], 'Title': i['Title'], 'Source': i['Source'],
                                          'Link': i['Link'], 'SHA-1': i['SHA-1'], 'SHA1': j,
                                          'Date': i['Date'], 'Year': i['Year']})
            for j in array['md5']:
                NEW_APT_reports.writerow({'Filename': i['Filename'], 'Title': i['Title'], 'Source': i['Source'],
                                          'Link': i['Link'], 'SHA-1': i['SHA-1'], 'MD5': j,
                                          'Date': i['Date'], 'Year': i['Year']})
        else:
            NEW_APT_reports.writerow({'Filename': i['Filename'], 'Title': i['Title'], 'Source': i['Source'],
                                      'Link': i['Link'], 'SHA-1': i['SHA-1'], 'Date': i['Date'], 'Year': i['Year']})
