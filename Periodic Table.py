periodicTableSymbols=[["H","B","C","N","O","F","P","S","K","V","Y","I","W","U"],['HE', 'LI', 'BE', 'NE', 'NA', 'MG', 'AL', 'SI', 'CL', 'AR', 'CA', 'SC', 'TI', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TI', 'PB', 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', 'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']]#chemical elements in order of number of letters and appearance
def checkLetter(letter):
  output=False
  if len(letter)==1:
    if letter in periodicTableSymbols[0]:
      output=letter
  else:
    if letter in periodicTableSymbols[1]:
      output=str(letter[0]+letter[1].lower())
  return(output)
def getResult(word):
  finalOutput=""
  if word=="":
    return("\n")
  elif checkLetter(word[0])!=False:
    return(getResult(word[1:]))
  else:
    return(False)
while True:
  word=input("Please enter a word")
  word=word.upper()
  getResult(word)
  
  
