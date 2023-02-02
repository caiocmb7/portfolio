## 🏆 World Cup 2022 Catar Project 

Credits to my team partner Marco Carujo for creating the [Dataset](https://www.kaggle.com/datasets/mcarujo/fifa-world-cup-2022-catar)

## Table of Contents
1. [Statistics of the 2022 World Cup in Qatar](#statistics)
2. [Activities](#activities)
3. [Problems](#problems)
4. [Views](#views)
5. [Conclusion](#conclusion)
6. [Next Steps](#next-steps)

<a name="statistics"></a>
## 📊 General statistics of the 2022 World Cup in Qatar
|        Event       | Total |
|-------------------|-------:|
|    Substitution    |  587  |
|     Yellow card    |  224  |
|        Goal        |  153  |
|         PK         |   41  |
|       Penalty      |   17  |
|   Disallowed goal  |   9   |
|   Missed penalty   |   6   |
| Second yellow card |   3   |
|      Own goal      |   2   |
|      Red card      |   1   |

<a name="activities"></a>
## 🔧 Activities

- Data cleaning

- Feature engineering for data manipulation (data transformation)

- Perform data analysis (EDA)
    1. SQL
    2. Pandas/Seaborn/Matplotlib/yellowbricks/etc
    3. pivottablejs

- Create a general statistics based on previously data analysis and feature engineering
    - Generated dataframes contained event_list statistics, global statistics, top scores, top assists, top participations, etc;

- Perform data clustering using k-means and DBScan

- Build ML Algorithms to predict home team winning, drawing or away team winning
    1. Train/test environment
    2. Cross Validation K-Fold
    3. GridSearch
    4. SVM, LogisticRegression and RandomForestClassifier results comparison
    5. Perform oversampling to develop the results

<a name="problems"></a>
## 🤔 Problems

* Columns with list of dictionary, we had to manipulate the csv to transform into new columns
    - this columns with a list of dictionary, have values like " Messi ", so we have to split this to be a correct value
    - based on the columns "lineup_home" and "lineup_away", we created 2 new columns for each columns to get the data from those columns, that will be better to understand.
    - based on the column "events_list", we created a new dataset that will be insume to create the "statistic dataset", which will contains values about yellow cards, goals, etc.
    
* Manipulation problems to generate new dataframes with the original dataset -> event_list statistics, global statistics, statistics per team, top scorer, top assists, top participations, etc;

* As the dataset is relatively small, with only 64 rows, when we conduct a prediction analysis using RandomForestClassifier, LogisticRegression, and SVM, we observe that the values of precision, accuracy, and recall remain consistent, regardless of whether we use grid search or k-fold cross-validation.

* Even using a loop to search for the best hyperparameters for DBScan, the values found are still poor based on the silhouette_score, davies_bouldin_score and calinski_harabasz_score metrics.

<a name="views"></a>
## 📈 Views

* Feature Engineering
    - Percentage dtype manipulation
    - Created a primary key (match_id) for the dataset
    - Transforming lineup_home and lineup_away columns which contains list of dictionaries into new columns
    - Transforming events_list column into a new dataframe that will be use for global statistics.
        - match_id related to the worldcup dataset (foreign key)
        - event_id as primary key
    - Check the numerical/float columns which will be used for predictions if they are gaussian distribuition
        - Apply log transformation

* Global statistics from each team (statistics per team), total of goals (top scorers), total of assists (top assistances), total team goals, etc;

* EDA Session
    - SweetViz 
    - Notebook analysis

* Ball possession for the 2022 World Cup was not a decisive factor in whether a team will win the match, as out of the 54 games that resulted in a win or loss for a team, only half (27) were determined by equality (ball possession and victory).

* Identified which players have the biggest impact on matches (games versus win percentage)

* Relationship between the number of goals scored and the number of shots on goal (Which teams were most effective in goal kicks)

* Predictions columns were analyzed to indicate if there was a upset case in the games.
    - In 64 games, we had 25 upset games (prediction not equals to the real winner of the game)
    - Despite the correlation between possession of the ball and the prediction of victory, this wasn't an indication in this case
        ("possesion_home" vs "prediction_team_home_win")

* Clustering by team statistics
    - K-means
    - DBScan
        - GridSearch for DBScan using metrics: silhouette_score, davies_bouldin_score, calinski_harabasz_score

* Build ML Algorithms using k-fold and gridsearch to predict home team winning, drawing or away team winning
    - LabelEncoder
    - Log Transformation
    - Standardize columns reduced the values of the metrics.
    - Compare results using SVM, LogisticRegression and RandomForestClassifier
        - Perfomed better when using more test size
        - K-fold cross validation increased the metrics
        - Oversampling using imblearn
            - Utilized in the train part
            - Without oversampling was better
        - yellowbrick confusion matrix
    - Feature Selection: Recursive Feature Elimination with Cross-Validation (RFECV) and Feature Selection based on Importance Weight (SFM)

<a name="conclusion"></a>
## 🏁 Conclusion

It was possible to carry out various actions in the context of Data Science from this project, facing several challenges along the way to effectively carry out the project. About it, it was possible to approach the entire data pipeline in a Data Science project to demonstrate my knowledge in the area

<a name="next-steps"></a>
## 🚀 Next Steps

Since the dataset in question is very small in the context of applying some techniques, even with oversampling, I believe that carrying out certain mentioned actions to really demonstrate its final form would be interesting. In this way, using a larger dataset in this context would be something relevant

