import random

def random_color():
  return random.choice("RGBW")

def get_code():
  result = ""
  for i in range(4):
   result = result + random_color()
  return result

code = get_code()
guess = input().upper()


#Look for exact matches
#Remove items that are exact matches
#Return C for each match
def look_for_exact(code, guess):
  result = ""
  new_code = ""
  new_guess = ""

  for i in range(4):
    if code[i] == guess[i]:
      result = result + "C"
    else: #did not match exactly
      new_code = new_code + code[i]
      new_guess = new_guess + guess[i]

  return result, new_code, new_guess

result, new_code, new_guess = look_for_exact(code, guess)

#Look for matches of color only
#Note: Exact matches have been removed
#Return a B for each color match
def match_for_color(result, new_guess, new_code):
  new_result = ""
  x = list(new_guess)
  y = list(new_code)
  for i in range(len(new_guess)):
    if x[i] in new_code:
      result = result + "D"
      new_result = result
      for j in range(len(new_code)):
        if x[i] == y[j]:
         y[j] = ""
        else:
         y[j] = y[j]
        new_code = y
    else:
     new_result = result + ""
  return new_result

#return hint based on code and guess  
# C: exact match B: color only match (not poss)
def hint(code, guess):
  pass

def main(code, guess):
  print(code)
  print(look_for_exact(code, guess))
  print(match_for_color(result, new_code, new_guess))
  
print(look_for_exact("GGGG", "GWGR"))
print(look_for_exact(code, guess))
main(code, guess)