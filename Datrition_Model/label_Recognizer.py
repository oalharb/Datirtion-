import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os
import glob
import re
import sys
import cv2
import post_process
import pandas as pd

def label_Recognizer(path):
    import re
    import os
    from matplotlib import pyplot 
    files = []
    for  r,d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(file))
    p = re.compile('[0-9]+.jpg')
    all_result = []
    for f in files:
        for file in glob.glob('./cropped/*.jpg'):
            bw = cv2.imread(file, 0)

        # Apply adaptive thresholding to images | @Suma Not Required already applied in image processing.
#             thresh = cv2.adaptiveThreshold(bw, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#                                            cv2.THRESH_BINARY, 11, 2)

        # Get text recognition from thresholded images
            output = pytesseract.image_to_string(Image.fromarray(bw))

            #fileName = p.findall(file)[0]
            #print ("Proccessing " + fileName)
            
            x = post_process.post_process(output)
            #print("\n Completed Labels for:", fileName, '\n', output)
            all_result.append(x)
            x['product_id']=file
        result = []
        for i in all_result:
            if len(i) == 0:
                pass
            else:
                result.append(i)
#        return result
         
        dx_nutrition = pd.DataFrame(result)
        dx_nutrition.product_id = dx_nutrition.product_id.apply(lambda x:x.replace('./cropped\\',''))
#         dx_nutrition.to_csv('Datrition_df.csv', index=False)
        return dx_nutrition
    