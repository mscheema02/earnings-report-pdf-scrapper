import pandas as pd
import matplotlib as plt
import requests
import tabula
import pdfquery


# df = pd.read_csv("file_path / file_name.")
filePath = "./er-testers/20220427_alphabet_10Q.pdf"
i = 0;


# pdf = pdfquery.PDFQuery('C:/Projs/earnings-report-pdf-scrapper/er-testers/20220427_alphabet_10Q.pdf')
# pdf.load()
i = 0
output = "last"
while(i < 5):
    print (i)
    i=i+1
print("... then the", output, "value is", str(i))

# import pandas as pd
# response = requests.get("http:/randomfox.ca/floof")
# print(response.status_code)