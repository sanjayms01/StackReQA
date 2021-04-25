# StackReQA




Note:
Data folder is not uploaded due to the large file sizes.

- master: contains general data processing notebooks and helper functions.

  - EDA.ipynb: exploratory data analysis on data
  - master_dictionaries.ipynb: creates dictionaries of question and 10 answer pairs and labels which answer is true (1) or false (0) for modeling purposes.
  - preprocessing_raw_data.ipynb: preprocessing of raw data for models
  - train_test_split.ipynb:  splits raw data into train/development/test
  
  - helper_functions: functional python files
    - bert_funcs.py: functions that return tokenized data for BERT's pretrained model
    - evaluation.py: functions that return metrics that evaluate model performance
    - parse.py: 
    - smiliarity_score_dicts.py: functions that return similarity scores of each predicted answers and returns answer rankings
