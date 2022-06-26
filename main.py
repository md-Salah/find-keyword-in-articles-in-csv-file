import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import os

def select_file():
    root = tk.Tk()
    root.withdraw()
    path_name = askopenfilename()
    root.destroy()
    return path_name

df = pd.read_csv(select_file())

keyword_categories = [
    ['operator', []],  #Names
    #Resource Estimates
    ['recoverable', ["recoverable resource", "remaining resource", "remaining recoverable", "resource", "boe", "bbl", "bo/d", "mcf", "bcf", "barrels", "oil equivalent", "production", "EUR"]], #Total/Remaining Recoverable Resource
    ['reserves', ["reserves"]], #
    ['ooip', ["OOIP", "Resource", "oil in place", "initial resource"]], #OOIP Resource
    #Development Parameters
    ['capacity', ["capacity", "throughput", "maximum production", "production limit", "peak rate", "peak", "peak production output"]], #platform capacity
    ['capex',["capital", "capex", "project cost", "total spend", "project spend", "capital expenditure", "expenditure", "development cost", "construction cost"]],
    ['opex', ["opex", "operating expense", "expense", "operating cost", "operational cost", "variable cost"]],
    ['fid', ["sanction", "final investment decision", "investment decision", "FID", "construction start"]], #FID Date
    ['firstprod', ["first production", "production date", "commencement", "commencing production"]], #First Production Date
    ['projectlife', ["project life", "estimated life", "projected life", "will produce for", "production life"]],
    ['discoverydate', ["discovered", "first well", "initial drilling", "frac date"]],
    ['prodwells', ["wells", "producers", "well", "development well", "producing wells", "production wells", "oil wells", "gas wells"]], #number of producing wells
    ['injwells', ["injector", "injection wells", "injection well"]], #number of injection wells
#
    ['emissions', ["emission", "emissions", "emission intensity", "emissions profile"]],
    ['interest', ["%", "working interest", "operator position", "consortium", "ownership interest", "interest"]] #Working Interest %
]

result = []
def keyword_match(df):
    for index, row in df.iterrows():
        article_body = row[17]
        # print(article_body)
        
        # hit_category = ''
        # hit_keywords = ''

        for x in keyword_categories:
            # category = x[0]
            # keywords = x[1]
            for keyword in x[1]:
                if keyword in article_body:
                    hit_keywords = keyword
                    hit_category = x[0]
                    result.append([row[12], row[6], row[0], hit_category, hit_keywords, row[3], row[1], article_body])
  
        # print(hit_category, hit_keywords)
        # os.system('pause')

keyword_match(df)
label = ['Field Name', 'Country', 'Article ID', 'Hit Category', 'Keyword', 'Article Type', 'Published Date', 'Article Body']
pd.DataFrame(result, columns=label).to_csv('output.csv', index=False) 