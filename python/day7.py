import random
from urllib.request import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

PHRASES = {
    "class %%%(%%%):":
       "Make a class named %%% that is-a %%%.",
    "class %%%:\n\tdef _init_(self, ***)":
       "class %%% has-a _init_ that takes self and *** params.",
    "class %%%:\n\tdef ***(self, @@@)":
       "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
       "set *** to an instance of class %%%.",
    "***.***(@@@)":
       "from *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
       "from *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
   PHRASE_FIRST = True
else:
   PHRASE_FIRST = False

for word in urlopen(word_url).readlines():
   words.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrase):
   class_names = [w.capitalize() for w in 
                   random.sample(words,snippet.count("%%%"))]
   other_names = random.sample(words,snippet.count("***"))
   results = []
   param_names = []

   for i in range(0, snippet.count("@@@")):
      param_count = random.randint(1,3)
      param_names.append(', '.join(
          random.sample(words, param_count)))

   for sentence in snippet, phrase:
      result = sentence[:]
      for word in class_names:
         result = result.replace("%%%", word, 1)

      for word in other_names:
         result = result.replace("***", word, 1)

      for word in param_names:
         result= result.replace("@@@", word, 1)
      
      results.append(result)

   return results

try:
   while True:
          snippets = list(PHRASES.keys())
          random.shuffle(snippets)

          for snippet in snippets:
             phrase = PHRASES[snippet]
             question, answer = convert(snippet, phrase)
             if PHRASE_FIRST:
                question, answer = answer, question 

             print(question)

             input(">")
             print(f"ANSWER: {answer}\n\n")            
except EOFError:
   print("\nBye")