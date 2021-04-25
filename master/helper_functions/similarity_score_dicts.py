def create_similarity_score_dict(qa_dict, embeddings_dict, similarity_score):
  """Create dictionary with keys that are question ids and values that are tuples of answer id and similarity (either dot product or cosine) score
  {'question_id' => [10 ('answer_id', cosine_similarity_score)]}
  
  qa_dict: a dictionary where keys are question ids and values are a list of 10 tuples, 
  where each tuple is an answer id and a 1 or 0 indicating whether that answer id is the correct answer for that question

  embeddings_dict: a dictionary where keys are question and answer ids and values are embeddings of that question/answer

  similarity_score: dot_product = calculates the dot product as the similarity score
                    cosine = calculates the cosine similarity as the similarity score
  """

  import numpy as np
  from numpy.linalg import norm
  
  similarity_score_dict = {}

  #Loop through all the question ids
  for key in qa_dict:
    #Get the embedding for that question
    question_embedding = embeddings_dict.get(key)

    #Add question id to cosine sim dict with empty list
    similarity_score_dict[key] = []

    #Get all answer ids
    answers = qa_dict.get(key)

    #Loop through the answer ids
    for item in answers: 

      #Get the embedding for the answer
      answer_embedding = embeddings_dict.get(item[0])

      if similarity_score == 'dot_product':
        
        #Take the dot product of question embedding and answer embedding
        similarity_score_value = np.inner(question_embedding, answer_embedding)

        #Add dot product value to dictionary
        similarity_score_dict[key].append((item[0], similarity_score_value[0][0]))

      elif similarity_score == 'cosine':
        
        # Calculate the cosine similarity of question embedding and answer embedding
        similarity_score_value = np.inner(question_embedding, answer_embedding) / (norm(question_embedding) * norm(answer_embedding))

        #Add cosine similarity score to dictionary
        similarity_score_dict[key].append((item[0], similarity_score_value))

  return similarity_score_dict
  
  

def compute_rankings(scores_dict):
  """Create dictionary with keys that are question ids and values that are tuples of answer id and cosine similarity score ranking
  {'question_id' => [10 ('answer_id', ranking)]}

  rankings_dict: a dictionary with keys that are question ids and values that are tuples of answer id and ranking
  """

  from scipy.stats import rankdata

  rankings_dict = {}

  # Loop through each question in the cosine similarity scores dict
  for key in scores_dict:

    # Get the list of tuples that are (answer_id, cosine similarity score)
    answer_scores = scores_dict.get(key)

    scores = [t[1] for t in answer_scores]
    #ranks = rankdata(scores)
    ranks = len(scores) - rankdata(scores).astype(int) + 1
    rankings = []

    for i in range(len(answer_scores)):
        rankings.append((answer_scores[i][0], ranks[i]))

    # # Sort and rank
    # sorted_scores = sorted(answer_scores,key=lambda x: x[1], reverse=True)
    # rankings = []
    # rank = 1
    # for k,v in groupby(sorted_scores, lambda x: x[1]): # group by score
    #   grp = [(tup[0], rank) for tup in v] # get item tup[0] and put it in a tuple with the rank
    #   rankings += grp
    #   rank += len(grp) # increase rank for next grouping
    
    rankings_dict[key] = rankings

  return rankings_dict
