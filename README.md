# StackReQA




**Note**:
Data folder is not uploaded to github due to their large file sizes.

# Folder Structure

- *master*: contains general data processing notebooks and helper functions.

  - *EDA.ipynb*: exploratory data analysis on data
  - *master_dictionaries.ipynb*: creates dictionaries of question and 10 answer pairs and labels which answer is true (1) or false (0) for modeling purposes.
  - *preprocessing_raw_data.ipynb*: preprocessing of raw data for models
  - *train_test_split.ipynb*:  splits raw data into train/development/test
  
  - *helper_functions*: functional python files
    - *bert_funcs.py*: functions that return tokenized data for BERT's pretrained model
    - *evaluation.py*: functions that return metrics that evaluate model performance
    - *parse.py*: 
    - *smiliarity_score_dicts.py*: functions that return similarity scores of each predicted answers and returns answer rankings

- *model_tfidf*: contains notebooks for the BM-25 model
  - *preprocessing_tfidf_baseline_data.ipynb*: creates processed data specifically for the BM-25 model
  - *tfidf_baseline.ipynb*: trains and evaluates data on the BM-25 model

- *model_word2vec*: contains notebooks for the Word2Vec models
  - *CosineSimilarity_Word2Vec_\**: evaluates the Word2Vec embeddings on cosine similarity scores
  - *word2vec_\**: creates various Word2Vec embeddings

- *reports*: contains our final report and slidedeck

- *use*: contains Universal Sentence Encoder (USE) models
  - *USE_Model_\**: different variations of USE models using the concatenated architecture
  - *USE_Two_Towers_\**: different variations of USE models using the concatenated architecture
  - *Dual_Encoder_Models*: evaluates the USE embeddings on dot product scores
  - *Monster_Model_\**: different mon
