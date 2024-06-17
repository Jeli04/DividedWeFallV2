# Divided We Fall 
Divided we fall is a revamp of a previous hackathon project made at Rose Hack in the very beginning of 2023.

`Read about our previous project here:`
https://devpost.com/software/divided-we-fall

## Overview
Divided We Fall's current state is a web application available for public use. With our project you can input a link to article, site, blog post, etc. As long as it is pubically viewable you can input an url, request an analysis, and recieve a score. This score will tell you potentially how bias the content of the link is. The bias report has no politically views or opinions it is an unbiased model that is trained and language data.

## Why did we build it?
Our team believes the current political state of the world is in shambles. The state of modern media has created immense political division. Today's 24/7 news channels and personalized social media streams not only affirm but also amplify our existing beliefs, deepening divisions and fostering bitterness toward differing viewpoints. We feel that having an unbiased model capable of showing you the potential bias in the media you consume is extremely important.

## How to use
Clone the repo\
Add your hugging face key into the .env file\
python -m venv venv\
.\venv\Scripts\activate  # Activate your virtual environment on Windows\
pip install flask lxml_html_clean  # Install Flask and the required lxml package within the venv\
pip install python-dotenv\
pip3 install flask\
pip3 install requests\
pip3 install bs4\
pip3 install newspaper3k\
python .\Webapp\board\ \__init__.py  # Run your Flask app\

Using our project is quite simple! Find a link, click, and view the bias scores! 

## Contact
If you face any sort of problems please feel free to contact us! Our githubs are under this project and also listed on the site. Our public social medias are listed under our githubs for contact purposes.
