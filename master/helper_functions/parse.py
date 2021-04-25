from bs4 import BeautifulSoup
import keyword 

def extractText(text):
  """
  Removes all code from the input text.
  Returns text without html tags.
  """
  soup = BeautifulSoup(text, 'html.parser')
  for code in soup.find_all('code'):
    code.decompose()
  return soup.get_text()

def extractCode(text):
  """Finds all code within input text and returns code without tags"""
  soup = BeautifulSoup(text, 'html.parser')
  code_str = str()
  for code in soup.find_all('code'):
    code_without_tags = code.get_text()
    code_str += code_without_tags
  return code_str

def extractContent(content):
  """Returns input content without html tags"""
  soup = BeautifulSoup(content, 'html.parser')
  return soup.get_text()

def extractReservedWords(code):
  """Returns all keyword/reserved words"""
  reserved_words=[]   #https://realpython.com/lessons/reserved-keywords/5646
  code = str(code).replace("\n", "")
  for c in code.split(" "): 
      if keyword.iskeyword(c): 
        reserved_words.append(c) 
  str1= " "
  return (str1.join(reserved_words))

def extractReservedWords_top50(code):
  """Returns all keyword/reserved words"""
  reserved_words=[]   #https://realpython.com/lessons/reserved-keywords/5646
  code = str(code).replace("\n", "")
  qa_top50_adjv2 = ['+', '<', 'of', '*', "'", '"', '==', 'File', '>', 'to', '#', '=', '+=', 'print', '%', '!=', '-', ':', 'i', 'x', 'line']
  for c in code.split(" "): 
      if keyword.iskeyword(c): 
        reserved_words.append(c) 
      elif c in qa_top50_adjv2:
        reserved_words.append(c)
      else:
        continue
  str1= " "
  return (str1.join(reserved_words))


