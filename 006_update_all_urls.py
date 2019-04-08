# Steo 6: Convert all urls to their final URLs
# Input: a master list of urls
# Output: an updated list of urls that moves rejects into one bucket, final
# urls into another bucket, saving tthe title along with it for good measure?

import requests
from time import sleep
from lxml.html import fromstring

# We're going to take this file, check through its contents, and sort it into
# success and failure files
listFile = open('./output/output_urls__unshorted-sorted.txt')
lines = listFile.readlines()
listFile.close()

# Set up success and failure output files
# output_file____full = open('./output/output_urls____full.txt', 'a')
# output_file____error = open('./output/output_urls____error.txt', 'a')

# Set up a tracker file; this will let us keep track of where we are at in the
# process in case the script fails mid-way through. First we read the current
# contents into a list, then we re-open it for saving purposes.
output_file__tracker = open('./output/tracker.txt', 'r')
tracker_lines = output_file__tracker.readlines()
output_file__tracker.close()

# output_file__tracker__output = open('./output/tracker.txt', 'a')

# Let's output a counter now and then
counter = 0

def update_counter():
    global counter

    counter += 1
    if (counter % 10 == 0):
        print('Counter: ' + str(counter))

# Here's our main flow
for line in lines:
    # First, let's check if we've already run this url
    if line not in tracker_lines:
        # It's not, so, we can try to get it. The top level try is there because
        # the request might break in a horrible way.
        url_to_get = line.replace('\n', '')

        try:
            res = requests.get(url_to_get)

            # If the request itself works, we need to check for the status code;
            # we might get a 404 instead of a bad error
            try:
                res.raise_for_status()

                # We seem to be okay; let's gather up some information, create
                # a little dictionary, and add it to our output file.
                tree = fromstring(res.content)
                title = tree.findtext('.//title')

                output = { title.strip(): res.url }

                output_file____full = open('./output/output_urls____full.txt', 'a')
                output_file____full.write(str(output))
                output_file____full.write('\n')
                output_file____full.close()

                # And we can append this line to our tracker file
                output_file__tracker__output = open('./output/tracker.txt', 'a')
                output_file__tracker__output.write(line)
                output_file__tracker__output.close()

                # Update the counter
                update_counter()

            except Exception as exc:
                print('# Error - There was a problem: %s' % (exc))
                output_file____error = open('./output/output_urls____error.txt', 'a')
                output_file____error.write('# Error - raise_for_status:\n')
                output_file____error.write('%s' % (exc))
                output_file____error.write('\n')
                output_file____error.write(line)
                output_file____error.write('\n')
                output_file____error.close()

                # And we can append this line to our tracker file
                output_file__tracker__output = open('./output/tracker.txt', 'a')
                output_file__tracker__output.write(line)
                output_file__tracker__output.close()

                # Update the counter
                update_counter()

            sleep(0.125)

        except Exception as excexc:
            output_file____error = open('./output/output_urls____error.txt', 'a')
            output_file____error.write('# Error - connectivity:\n')
            output_file____error.write(line)
            output_file____error.write('\n')
            output_file____error.close()

            # And we can append this line to our tracker file
            output_file__tracker__output = open('./output/tracker.txt', 'a')
            output_file__tracker__output.write(line)
            output_file__tracker__output.close()

            # Update the counter
            update_counter()

        sleep(0.125)

# output_file____full.close()
# output_file____error.close()
