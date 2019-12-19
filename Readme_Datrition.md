# Project Name: Datrition (Data Nutrition = Datrition)

# Team Members: Mansour Aljuaid, Omar Alharbi, Sumaiah Alsadhan


### What is your problem statement?  What will you actually be doing?

Reading product images, detecting, and extracting Nutrition Facts Label is a challenging task for regulators and consumers. This is something that has been learned during the Datathon of Saudi Food and Drug Authority (SFDA). SFDA is looking for an open source solution that address thier problem and help them better regulate the local market. Our project aims to work with thier data and develop a model that will help them address this issue. 

The project pipeline is going to consist of three stages, namely; Image Preprocessing, Image Processing, and Postprocessing. The intention is to take this further and try to address the challenge of reading product images in different languages of countries that are the main places of importation such as Chinese, Japanese etc and different nutrition facts labels' format.

### Who is your audience?  Why will they care?

The main targeted audiance are authority bodies such as SFDA and Saudi Customs. However, the final product could be used by wholesale and retail industry; and consumers as well. SFDA cares because this tool could help them improve thier registeration process, plus, enable them regulate the local maket more efficently. Wholesale and Retail industry could use it for analysis purposes. Consumers could use it to aid thier selection decision-making.  

### What is your success metric?  How will you know if you are actually solving the problem in a useful way?

The sucess metric, the model ability to read any unknown product images. If there is a growing demand for the solution then we will know that it solved the problem in a successful way. But, also, we will gather feedback especially from SFDA.

### What is your data source?  What format is your data in?  How much cleaning and munging will be required?

The data source is Open Data [https://data.gov.sa/Data/en/dataset/food-products-pictures-from-saudi-food-drug-authority].

### What are potential challenges or obstacles and how will you mitigate them?

At this stage, the following are the expected potential challenges: 
1. The detection of the text in the images in a way that ensures the consistancy of our accuracy for different images in different resolutions and orientation. (The use of different techniques to generalize our model to make it able to deal with different images and languages could be a way to mitigate this)
2. The accurate capture of the required text within the Nutrition Facts Label. (Tackling the challenge in phases/stages is an approach to resolve this)

### Is this a reasonable project given the time constraints that you have?

Yes, we believe that there is enough time to understand this problem and provide a suitable model. 

### Here is our public Git Hub REPO link
https://github.com/aljuaidm/Datrition
