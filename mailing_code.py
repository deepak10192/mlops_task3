#!/usr/bin/env python
# coding: utf-8

# In[16]:


import smtplib


# In[17]:


from email.mime.multipart import MIMEMultipart


# In[18]:


from email.mime.text import MIMEText


# In[19]:


mail_content ='''
ACCURACY_OF_MODEL
'''


# In[20]:


sender_address = 'senderemail@gmail.com'
sender_pass = 'password'
receiver_address = 'receiveremail@gmail.com'


# In[21]:


message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'accuracy model status'


# In[23]:


message.attach(MIMEText(mail_content,'plain'))


# In[ ]:


attach_file_name = 'accuracy.txt'


# In[ ]:


attach_file = open(attach_file_name,'rb')


# In[ ]:


payload = MIMEBase('application','octate-stream')


# In[ ]:


payload.set_payload((attach_file).read())


# In[ ]:


encoders.encode_base64(payload)


# In[ ]:


payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)


# In[24]:


session = smtplib.SMTP('smtp.gmail.com',587)


# In[25]:


session.starttls()


# In[26]:


session.login(sender_address,sender_pass)


# In[27]:


text = message.as_string()


# In[28]:


session.sendmail(sender_address,receiver_address, text)


# In[29]:


session.quit()


# In[30]:


print('Mail Sent')


# In[ ]:




