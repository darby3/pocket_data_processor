# Steo 3: Get all the "short" urls and simply sort them out into a file
# Input: The output_urls.txt file from step 1
# Output: Put the clean urls in output_urls__clean.txt;
#         Put the short urls in output_urls__short.txt
#
# Note: no actual url fetching done at this time; just sorting so that we can
#       handle the actual fetching in another step, and keep track of where we
#       are at / having problems in the process

import re
import operator
import requests

listFile = open('./output_urls.txt')
lines = listFile.readlines()
listFile.close()

url_pattern = re.compile(r'https?://(.+?)/')

short_urls = [ 't.co', 'bit.ly', 'ow.ly', 'buff.ly', 'cdm.link', 'dlvr.it', 'fb.me', 'goo.gl', 'dev.to', 'wp.me', 'j.mp', 'is.gd'  ]

output_file__clean = open('output_urls__clean.txt', 'w')
output_file__short = open('output_urls__short.txt', 'w')

for line in lines:
    url_result = url_pattern.search(line)
    if (url_result):
        url_result_site = url_result.group(1)
        if (url_result_site in short_urls):
            output_file__short.write(line)
        else:
            output_file__clean.write(line)

output_file__clean.close()
output_file__short.close()
