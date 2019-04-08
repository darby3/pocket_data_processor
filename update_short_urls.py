# Steo 4: Take all the short URLs and turn them into real URLs
# Input: The output_urls__short.txt file from step 3
# Output: Put the new urls in output_urls__short__full.txt;

import requests
from time import sleep

listFile = open('./output_urls__short.txt')
lines = listFile.readlines()
listFile.close()

output_file__short__full = open('output_urls__short__full.txt', 'a')
output_file__short__error = open('output_urls__short__error.txt', 'a')

for line in lines:
    url_to_get = line.replace('\n', '')
    try:
        res = requests.get(url_to_get)

        try:
            res.raise_for_status()
            # print(res.url)

            output_file__short__full.write(res.url)
            output_file__short__full.write('\n')

        except Exception as exc:
            print('There was a problem: %s' % (exc))
            output_file__short__error.write(line)

        sleep(0.25)

    except Exception as exc:
        print('There was a problem: %s' % (exc))
        output_file__short__error.write(line)

output_file__short__full.close()
output_file__short__error.close()
