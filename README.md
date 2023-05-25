# Microscripts
These are some of my micro level, quality of life scripts I use on the daily/weekly. They're tailored to my specific useage and I whip them up kind of quickly, but hopefully someone finds them useful. 

## loginator
A .tsv file is generated every hour, so this concatenates them into one big text file. Set the input and output folder and run.

## pdfinator
My company uses Nitro to convert images into pdf files, but it's slow and crashes with large loads. This takes the most common file types we see and converts them into pdf pretty quickly.

## logininator
Not to be confused with loginator. Opens the two sites I use every morning. Quite shoddy. It doesn't work how I want because it closes the browser window when the script is done, unless I have input('Press ENTER to exit) but the console window is annoying. But it's fun to practice with Selenium and uc options.

## reportinator
My company downloads a salesforce report semiweekly to use for analysis. This script runs twice a week, downloads the needed reports, and replaces the old reports with a new file and updated file name on our shared drive. I took out the duplicate code for the other reports and just kept one.
