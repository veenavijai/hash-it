import io
import os,sys
import csv
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
  
credential_path = "C:\\Users\\Dell\\Desktop\\Hacktech\\HT.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
keywords=[]
# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
folder_path = os.getcwd()
print(folder_path)
with open('img_paths.txt') as f:
    read= f.readlines()
f.close()
reader=csv.reader(read)

for lines in reader:
    line = lines[0]
    
#file_names = ['ht1.jpg', 'ht2.jpg', 'ht3.jpg', 'ht4.jpg', 'ht5.jpg', 'ht6.jpg', 'ht7.jpg', 'ht8.jpg']
    file_paths = os.path.join(folder_path, line) 


    # Loads the image into memory
    with io.open(line, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

# Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
        keywords.append(label.description)
        
        
    print(keywords)
    
unique_string=(" ").join(keywords)

    
comment_words = ' '
stopwords = set(STOPWORDS) 
  
# iterate through the csv file 
#for val in key: 
      
    # typecaste each val to string 
   # val = str(val) 
  
    # split the value 
    #tokens = val.split() 
      
    # Converts each token into lowercase 
    #for i in range(len(tokens)): 
        #tokens[i] = tokens[i].lower() 
          
    #for words in tokens: 
    #comment_words = comment_words + words + ' '
  
  
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10
                ).generate(unique_string)
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 

plt.savefig('try1.png', bbox_inches='tight')
plt.close()