
# coding: utf-8

# In[8]:


#Input a string and format the string as required
Orig_str="WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
print("The original string is\n"+Orig_str+"\n")
split_str=Orig_str.split(',')
split_str
Formt_str=split_str[5].split('and')
print("The formatted string is\n" + split_str[0] +","+split_str[1]+"\n"+ split_str[2] +" !"+"\n"+split_str[3]+","+split_str[4]+ ","+Formt_str[0]+"\n"+'and'+Formt_str[1]+":")
    


