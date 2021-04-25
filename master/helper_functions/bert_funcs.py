import numpy as np

def bert_encode_content(content, tokenizer, max_length=512):
  content_tokens = []
  content_masks = []
  content_segments = []

  tokenized_text = tokenizer.tokenize(content)

  tokenized_text = tokenized_text[-(max_length-2):]
  sequence = ['[CLS]'] + tokenized_text + ['[SEP]']
  padding_length = max_length - len(sequence)

  tokens = tokenizer.convert_tokens_to_ids(sequence) + [0] * padding_length
  padding_masks = [1] * len(sequence) + [0] * padding_length
  segment_ids = [0] * max_length

  content_tokens.append(tokens)
  content_masks.append(padding_masks)
  content_segments.append(segment_ids)

  return np.array(content_tokens), np.array(content_masks), np.array(content_segments)


def bert_encode_content_beg_end(content, tokenizer, max_length=512):
  content_tokens = []
  content_masks = []
  content_segments = []

  tokenized_text = tokenizer.tokenize(content)
    
  #Only keep beginning and end tokens.  
  #If content has less than max_length (minus 2 for cls and sep) tokens, keep entire content.
  if len(tokenized_text) < max_length-2:
    tokenized_text=tokenized_text
  else:
    tokenized_text = tokenized_text[0:(int(max_length/2) - 1)] + tokenized_text[-(int(max_length/2) - 1):]
  
  sequence = ['[CLS]'] + tokenized_text + ['[SEP]']
  padding_length = max_length - len(sequence)

  tokens = tokenizer.convert_tokens_to_ids(sequence) + [0] * padding_length
  padding_masks = [1] * len(sequence) + [0] * padding_length
  segment_ids = [0] * max_length

  content_tokens.append(tokens)
  content_masks.append(padding_masks)
  content_segments.append(segment_ids)

  return np.array(content_tokens), np.array(content_masks), np.array(content_segments)


  # for text in content:
  #   tokenized_text = tokenizer.tokenize(text)

  #   tokenized_text = tokenized_text[-(max_length-2):]
  #   sequence = ['[CLS]'] + tokenized_text + ['[SEP]']
  #   padding_length = max_length - len(sequence)

  #   tokens = tokenizer.convert_tokens_to_ids(sequence) + [0] * padding_length
  #   padding_masks = [1] * len(sequence) + [0] * padding_length
  #   segment_ids = [0] * max_length

  #   content_tokens.append(tokens)
  #   content_masks.append(padding_masks)
  #   content_segments.append(segment_ids)