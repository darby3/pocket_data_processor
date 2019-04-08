# Steo 2: Get a summary view of the sites represented by the URLs
# Input: the output_urls.txt from step 1
# Output: A sorted view of a dictionary in output_sites.txt

import re
import operator

listFile = open('./output_urls.txt')
lines = listFile.readlines()
listFile.close()

output_file = open('output_sites.txt', 'w')
url_pattern = re.compile(r'https?://(.+?)/')
sites = {}

for line in lines:
    url_result = url_pattern.search(line)
    if (url_result):
        url_result_site = url_result.group(1)
        if (url_result_site in sites.keys()):
            sites[url_result_site] += 1
        else:
            sites[url_result_site] = 1

sorted_list = sorted(sites.items(), key=operator.itemgetter(1))

for site in sorted_list:
    output_file.write(str(site))
    output_file.write('\n')

output_file.close()
print(sites)
