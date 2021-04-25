def calculate_mrr(qa_dict, value_ranking_dict):
  """Function to calculate MRR

  qa_dict: a dictionary where keys are question ids and values are a list of 10 tuples, 
  where each tuple is an answer id and a 1 or 0 indicating whether that answer id is the correct answer for that question
  
  value_ranking dict: a dictionary where keys are question ids and values are a list of 10 tuples,
  where each tuple is an answer id and its dot product ranking for that question id """

  mrr_list = []

  #Loop through all the question ids
  for key in qa_dict:
    answers = qa_dict.get(key)

    #Get the correct answer id
    for item in answers:
      if item[1] == 1:
        correct_answer_id = item[0]
        break
      else:
        continue

    #Get the dot ranking of that answer for that question
    dot_product_rankings = value_ranking_dict.get(key)
    for item in dot_product_rankings:
      if item[0] == correct_answer_id:
        mrr_list.append(1/item[1])
        break
      else:
        continue

  mrr = sum(mrr_list)/len(mrr_list)
  print("MRR:", mrr)
  return mrr

def calculate_accuracy(qa_dict, value_ranking_dict):
  """Function to calculate accuracy

  qa_dict: a dictionary where keys are question ids and values are a list of 10 tuples, 
  where each tuple is an answer id and a 1 or 0 indicating whether that answer id is the correct answer for that question
  
  value_ranking dict: a dictionary where keys are question ids and values are a list of 10 tuples,
  where each tuple is an answer id and its dot product ranking for that question id """

  #Calculate accuracy
  correct_counter = 0
  incorrect_counter = 0
  total_counter = 0

  #Loop through all the question ids
  for key in qa_dict:
    answers = qa_dict.get(key)

    #Get the correct answer id
    for item in answers:
      if item[1] == 1:
        correct_answer_id = item[0]
        break
      else:
        continue

    #Get the dot ranking of that answer for that question
    dot_product_rankings = value_ranking_dict.get(key)
    for item in dot_product_rankings:
      if item[0] == correct_answer_id:
        if item[1] == 1:
          correct_counter += 1
          total_counter += 1
        else:
          incorrect_counter += 1
          total_counter += 1
        break
      else:
        continue

  print("Number correct:", correct_counter)
  print("Number incorrect", incorrect_counter)
  print("Total:", total_counter)
  print("Accuracy:", correct_counter/total_counter*100)
  return correct_counter/total_counter*100
  
 

def calculate_metrics(qa_dict, value_ranking_dict):
    """Function to calculate metrics

    qa_dict: a dictionary where keys are question ids and values are a list of 10 tuples, 
    where each tuple is an answer id and a 1 or 0 indicating whether that answer id is the correct answer for that question
  
    value_ranking dict: a dictionary where keys are question ids and values are a list of 10 tuples,
    where each tuple is an answer id and its dot product ranking for that question id """
    
    prediction_labels_dict = {}
    for key in value_ranking_dict:
      prediction_labels_dict[key] = []
      answers = value_ranking_dict.get(key)
      for item in answers:
        if item[1] == 1:
          prediction_labels_dict[key].append((item[0],1))
        else:
          prediction_labels_dict[key].append((item[0],0))
    
    #Count true positives
    TP = 0
    #Count false positives
    FP = 0
    #Count false negatives
    FN = 0
    #Count true negatives
    TN = 0

    for key in qa_dict:
      answers = qa_dict.get(key)

      #Get the correct answer id
      for item in answers:
        if item[1] == 1:
          correct_answer_id = item[0]
          break
        else:
          continue

      
      #Get the ranking of that answer for that question
      predictions_labels_dict = prediction_labels_dict.get(key)
      for item in predictions_labels_dict:
        if item[0] == correct_answer_id:
          if item[1] == 1:
            TP += 1
          else:
            FN += 1
          
        else:
          if item[1] == 1:
            FP += 1
          else:
            TN += 1

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    accuracy = (TP + TN) / (TP + FP + FN + TN)
    
    print("TP:", TP)
    print("FP:", FP)
    print("TN:", TN)
    print("FN:", FN)
    print("Precision:", precision)
    print("Recall:", recall)
    print("Accuracy:", accuracy)

    return precision, recall, accuracy