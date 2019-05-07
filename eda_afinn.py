import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from afinn import Afinn

def afinn_analysis(df):
    """
    initialize afinn sentiment analyzer and do afinn analysis on our data
    """
    af = Afinn()

    # compute sentiment scores (polarity) and labels
    sentiment_scores = [af.score(article) for article in df['text']]
    sentiment_category = ['positive' if score > 0 
                              else 'negative' if score < 0 
                                  else 'neutral' 
                                      for score in sentiment_scores]


    # sentiment statistics per news category
    df = pd.DataFrame([list(df['label']), sentiment_scores, sentiment_category]).T
    df.columns = ['label', 'sentiment_score', 'sentiment_category']
    df['sentiment_score'] = df.sentiment_score.astype('float')
    # print(df.groupby(by=['label']).describe())
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
    sp = sns.stripplot(x='label', y="sentiment_score", 
                       hue='label', data=df, ax=ax1)
    bp = sns.boxplot(x='label', y="sentiment_score", 
                     hue='label', data=df, palette="Set2", ax=ax2)
    fc = sns.catplot(x="label", hue="sentiment_category", 
                    data=df, kind="count", 
                    palette={"negative": "#FE2020", 
                             "positive": "#BADD07", 
                             "neutral": "#68BFF5"})
    t = f.suptitle('Visualizing News Sentiment', fontsize=14)