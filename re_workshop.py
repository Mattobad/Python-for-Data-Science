import re
import csv

with open("data/apache_log.txt") as f:    
    contents = f.read()
    

print(contents)
re_matches = re.findall('(\d+\.\d+\.\d+\.\d+)\s-\s-\s-\[(.+)\]',contents)

print(re_matches)

with open("results.csv","w") as f:
         csv_obj=csv.writer(f)
         csv_obj.writerows(re_matches)
