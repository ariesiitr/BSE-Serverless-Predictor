import json
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
from datetime import date
from datetime import timedelta
from bsedata.bse import BSE
    


print("fda")

print("fda")
bsedata = BSE()
# to execute "updateScripCodes" on instantiation
bsedata = BSE(update_codes = True)



#import pandas as pd
from bselib.bse import BSE
bselib = BSE()

today = date.today()
#print("Today's date:", today)

cnt=0
price={}
for company in bsedata.getScripCodes():
    try:
        q=bselib.quote(company)["stockPrice"]
        price[company]=q
        #print(company,cnt)
        cnt=cnt+1
    except:
        continue
        
    if(cnt>5):
        break



# In[4]:


close=pd.DataFrame(list(price.items()),columns = ["Company_Code",today])
close_transposed = close.T
#close_transposed.to_excel("close.xlsx")
print(close_transposed)


# In[ ]:




    
