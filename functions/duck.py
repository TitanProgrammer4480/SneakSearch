from duckduckgo_search import DDGS

def duck_search(s_term, s_num, s_region):
  if s_region == "":
    s_region = "wt-wt"
  results = DDGS().text(s_term, region=s_region, safesearch='off', timelimit='y', max_results=s_num)
  return results