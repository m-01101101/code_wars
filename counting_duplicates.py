# Write a function that will return the count of 
# distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# my answer
def duplicate_count(text):
    text = text.lower()
    b = []
    c = []
    for i in text:
        c.append(i)
    for i in c:
        b.append(c.count(i))
    d = dict(zip(c, b))
    appears = [i for i, occurrences in d.items() if occurrences > 1]
    return len(appears)
	
# answers i liked	
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
  
# lesson - get better at list comprehension  
