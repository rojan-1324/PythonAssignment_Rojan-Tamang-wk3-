def word_frequency(text):

 text=text.lower()

 for ch in ",.!?":
  text=text.replace(ch,"")

 words=text.split()

 counts={}

 for word in words:

  if word in counts:
   counts[word]=counts[word]+1

  else:
   counts[word]=1

 sorted_words=sorted(counts.items(),key=lambda x:x[1],reverse=True)

 print("Top 3 words:")

 for word,count in sorted_words[:3]:
  print(word,"-",count,"times")


text="""
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

word_frequency(text)