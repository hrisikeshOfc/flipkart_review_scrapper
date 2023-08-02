# Flipkart Review Scrapper
This is a flask based app to scrap user reviews and comments from a retail website and generates word-cloud with CSV data. 
The data that was gathered is available to download as well.


## Prerequisites

1. Environment setup.
```commandline
conda create --prefix ./env python=3.8 -y
conda activate ./env
```
2. Install Requirements
```commandline
pip install -r requirements.txt
```
3. Run setup to make internal packages usable
```commandline
pip install -e .
```
4. Run App 
windows
```commandline
python app.py 
```
Mac/linux
```commandline
python3 app.py 
```

## Docker  Integration 

1. Build Image 
```
docker build -t Image_name .
```
2. Create and run container
```
docker run -p 8000:8080 Image_name
```
3. Stop running container
```
docker stop container_ID
```
4. Start container 
```
docker start container_ID
```
## Flow Chart
![flowchart](flowchart/Scraper_Flowchart.png)

## Project Folder structure
```.
├── scraper/
│   ├── data_access/
│   │   ├── __init__.py
│   │   └── data_access.py
│   ├── enitity/
│   │   ├── __init__.py
│   │   └── entity.py
│   ├── exception/
│   │   ├── __init__.py
│   │   └── exception.py
│   ├── logging/
│   │   ├── __init__.py
│   │   └── logging.py
│   ├── logic/
│   │   ├── __init__.py
│   │   └── business_logic.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── tests.py
│   └── utils/
│       └── __init__.py
└── __init__.py
```
 
## Running the project
Navigate to scrapper/tests/tests.py
```commandline
python tests.py
```
Be sure that your app is running.
Results after running tests.py



## Interface 
![image](https://user-images.githubusercontent.com/40850370/162748874-f5de450f-e54f-4d39-bc9f-8ecac6b0be7c.png)
![image](https://user-images.githubusercontent.com/40850370/162749012-f64d09e2-ca72-41e5-81ad-12175a5877f8.png)

## Built With

1. FastApi 
2. Python
3. Html 
4. Css
5. shell script

## Authors
iNeuron Private limited
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
