
# coding: utf-8

# In[13]:


text=input("please type anything:\n")
counter = dict={}
while True:
    for ch in text:
        if ch in counter:
            counter[ch]+=1
        else:
            counter[ch]=1
    break
for ch,count in counter.items():
    print('"'+ch+'":',count)

