import os
import re as regex

"""
#%% divides the program into individual cells
"""
results =os.popen("ping -n 5 cs.smu.ca").read()
# %%
re_results = regex.findall('Average\s\=\s(\d+)',results)

print("Average time is:",re_results)

# %%
print("test")
