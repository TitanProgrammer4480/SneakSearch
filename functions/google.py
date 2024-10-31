from googlesearch import search

def g_search(s_term, s_num, s_region):
  return search(s_term, num_result=s_num, region=s_region, advanced=True)