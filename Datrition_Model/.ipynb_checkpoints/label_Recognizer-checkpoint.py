{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pytesseract\n",
    "from PIL import Image, ImageEnhance, ImageFilter\n",
    "import os\n",
    "import glob\n",
    "import re\n",
    "import sys\n",
    "import cv2\n",
    "import post_process\n",
    "\n",
    "def label_Recognizer(path):\n",
    "    import re\n",
    "    import os\n",
    "    from matplotlib import pyplot \n",
    "    files = []\n",
    "    for  r,d, f in os.walk(path):\n",
    "        for file in f:\n",
    "            files.append(os.path.join(file))\n",
    "    p = re.compile('[0-9]+.jpg')\n",
    "    all_result = []\n",
    "    for f in files:\n",
    "\n",
    "        for file in glob.glob('img_result/*.jpg'):\n",
    "            bw = cv2.imread(file, 0)\n",
    "\n",
    "        # Apply adaptive thresholding to images | @Suma Not Required already applied in image processing.\n",
    "#             thresh = cv2.adaptiveThreshold(bw, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\\\n",
    "#                 cv2.THRESH_BINARY, 11, 2)\n",
    "\n",
    "        # Get text recognition from thresholded images\n",
    "            output = pytesseract.image_to_string(Image.fromarray(bw))\n",
    "\n",
    "            fileName = p.findall(file)[0]\n",
    "            print (\"Proccessing \" + fileName)\n",
    "\n",
    "            x = post_process.post_process(output)\n",
    "            print(\"\\n Completed Labels for:\", fileName, '\\n', output)\n",
    "            all_result.append(x)\n",
    "            x['product_id']=file\n",
    "        result = []\n",
    "        for i in all_result:\n",
    "            if len(i) == 0:\n",
    "                pass\n",
    "            else:\n",
    "                result.append(i)\n",
    "        return result"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
