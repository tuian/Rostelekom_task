import PyPDF2
import re
import json
import requests
import os

# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from io import StringIO
#
# rsrcmgr = PDFResourceManager()
# retstr = StringIO()
# codec = 'utf-8'
# laparams = LAParams()
# device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
# fp = open('2011/Alerts DL-2011 Alerts-A-2011-02-18-01 Night Dragon Attachment 1', 'rb')
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# password = ""
# maxpages = 0
# caching = True
# pagenos = set()
#
# for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
#                               check_extractable=True):
#     interpreter.process_page(page)
#
# text = retstr.getvalue()
#
# fp.close()
# device.close()
# retstr.close()

p = re.compile('\b[0-9a-f]{40}\b')

github_url = "https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.json"
APTnotes = requests.get(github_url)
#
# pdfFile = open('2011/Alerts DL-2011 Alerts-A-2011-02-18-01 Night Dragon Attachment 1', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# print(pdfReader.getPage(0).extractText())
if APTnotes.status_code == 200:
    # Load APT report metadata into JSON container
    APT_reports = json.loads(APTnotes.text)
    # print(APT_reports[i]['Filename'])
    hashInPdf = {}
    for i in APT_reports:
        try:
            filename = i['Filename']
            year = i['Year']
            path = os.path.join(year, filename)
            # print(path)
            pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))

            for pageNumber in range(pdfReader.numPages):
                val = p.search(pdfReader.getPage(pageNumber).extractText())
                if val:
                    print('hash find success' + i, os.path.join(year, filename))
        except Exception as e:
            print(e)  # for i in len(hashInPdf):
