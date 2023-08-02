import yaml
import os 
from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go
import pandas as pd

config_path = os.path.join(os.getcwd(), 'config', 'config.yaml')

def read_config(config_path=config_path):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)

    return content
