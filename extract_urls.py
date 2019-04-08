# Step 1: Pull all the URLs from the Pocket export file
# Input: the export html file
# Output: output_urls.txt

import re

listFile = open('./ril_export__safe.html')
lines = listFile.readlines()
listFile.close()

output_file = open('output_urls.txt', 'a')
url_pattern = re.compile(r'href="(https?://.+?)"')

for line in lines:
    url_result = url_pattern.search(line)
    if (url_result):
        output_file.write(url_result.group(1))
        output_file.write('\n')

output_file.close()
