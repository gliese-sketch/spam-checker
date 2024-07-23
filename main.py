# Create a function that checks weather if a given
# sentence is spam or not

# give me a list of 30 spam keywords like gaming, betting, earning, crypto, etc. for learning purposes

# give me these keywords in comma seperated way, i want them for my python spam detector function
# f = open('keywords.txt', 'r')
# print(f.read())
# f.close()
data = None

try:
  with open('keywords.txt', 'r') as f:
    data = f.read()
except FileNotFoundError:
  print("File not found!")


def spam_check(sentence, spam_list):
  sentence = sentence.lower()
  for word in spam_list:
    if word.lower() in sentence:
      print('Marked as spam!')
      return True
  print('The given sentence is safe.')    
  return False

# x = "hey there i am good".split(' ')
# for word in x:
#   print(word)

x = spam_check('Hey there I am playing Rummy', data.split(', '))
print(x)