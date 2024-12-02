"""
from brave import Brave

def brave_search(s_term, s_num):
  brave = Brave()
  s_results = brave.search(q=s_term, count=s_num)
  print(s_results.web_results)
  return s_results.web_results
"""
