# StackReQA


### Abstract
Retrieval Question-Answering (ReQA) tasks identify the most relevant answer to a question. This paper presents StackReQA, which retrieves the most relevant answer to a given Stack Overflow question. We provide a solution that utilizes both the text and code of an input question in order to predict the most useful and appropriate answer. We present several approaches using different embeddings, ordering techniques, and architectures. Specifically, we embed the data using the Universal Sentence Encoder (USE), Bidirectional Encoder Representations from Transformers (BERT), Word2Vec and various combinations of these embeddings. We experiment with the ordering of questions and answers and text and code. Additionally, we compare models utilizing a dual encoder architecture and neural networks with early versus late fusion. We find that our models utilizing USE embeddings perform best. Specifically, our best-performing model embeds the data as is with USE and uses a late fusion neural network architecture.



# Folder Structure

**Note**:
Data folder is not uploaded to github due to their large file sizes.

- *bert*: contains Bidirectional Encoder Representations from Transformers (BERT) models
  - *model_bert_baseline*: evaluates different BERT embeddings with cosine similarity scores
  - *model_bert_concatenated_\**: different variations of BERT models using the concatenated architecture
  - *model_bert_two_towers_\**: different variations of BERT models using the two-towers architecture
  - *model_bert_hidden_states_\**: different variations of BERT models using BERT hidden states embeddings

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
  - *USE_Two_Towers_\**: different variations of USE models using the two-towers architecture
  - *Dual_Encoder_Models*: evaluates different USE embeddings with dot product scores
  - *Monster_Model_\**: different variations of combined embeddings model


