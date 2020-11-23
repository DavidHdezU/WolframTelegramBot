import wolframalpha

class WolframSearcher():
  """
  A class to search all type of things in Wolfram Alpha, including mathematics

  """
  def __init__(self, token):
    """
    Creates an instance of WolframSearcher

    Args:
        token {String}: The API Token to make requests to Wolfram Alpha
    """
    self.searcher = wolframalpha.Client(token)

  def search(self, text):
    """
    Search on Wolfram Alpha the information required

    Args:
        text {String}: The question to search on Wolfram Alpha

    Returns:
        String : The answer from Wolfram Alpha
    """
    res = self.searcher.query(text)

    if res['@success'] == 'false':  # Check if the question has an answer
      return "Can't find information"

    result = ''
    question = res['pod'][0]
    answer = res['pod'][1]

      # checking if pod1 has primary = true or title = result|definition
    if (('definition' in answer['@title'].lower()) or ('result' in  answer['@title'].lower()) or (answer.get('@primary','false') == 'true')):
      result = self.resolveListOrDict(answer['subpod'])
    else:
        result = self.resolveListOrDict(question['subpod'])
      
    return result
  
  def resolveListOrDict(self, variable):
    """
    An auxiliary fuction to verify if a variable is a Map or a List

    Args:
        variable {Map or List}: The question or answer provided by Wolfram Alpha

    Returns:
        String: The plaintext from the data of the request made 
    """
    if isinstance(variable, list):
      return variable[0]['plaintext']
    else:
      return variable['plaintext']

