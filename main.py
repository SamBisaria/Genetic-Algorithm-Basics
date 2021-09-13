import math, threading, time, random, string
spaces = [" ","\t","\n"]

word = random.choice()
threads = []
numchildren = 25
numgenerations = 1000

def parse(text):
  words = []
  start = 0
  for cur, char in enumerate(text):
    if text[start] in spaces:
       start = cur
    if char in spaces :
      word = text[start:cur]
      words.append(word) 
      start = cur 
  if start < len(text):
    word = text[start:]
    words.append(word) 
  return words

def bubbleSort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j].fitness > arr[j + 1].fitness :
              arr[j], arr[j + 1] = arr[j + 1], arr[j]

class myThread (threading.Thread):
  def __init__(self, threadID, name, generation, length):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.generation = generation
    self.length = length
    self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    self.weights = [1/26]*26
    self.fitness = 0
  def run(self):
    for i in range(26):
      r = random.randint(1,10)
      if r == 3:
        self.weights[i] += 0
      else:
        self.weights[i] -= 0.00
    wordGuess = random.choices(self.alphabet, weights = self.weights, k = self.length)
    for i in range(self.length):
      if wordGuess[i] == word[i]:
        self.fitness += 1
        self.weights[self.alphabet.index(word[i])] += 0.01
      elif wordGuess[i] != word[i]:
        self.weights[self.alphabet.index(wordGuess[i])] -= 0.001
    self.generation+=1
  def copythread(self, other):
    self.generation = other.generation
    self.length = other.length
    self.weights = other.weights

def main():
  global word, threads  
  for t in threads:
    t.start()
  for t in threads:
    t.join()  
  bubbleSort(threads)
  if threads[0].generation % 100 == 0:
    print("Generation: " + str(threads[0].generation))
    for t in threads:
      print (str(t.name) + ": " + str(t.fitness))
  if threads[0].generation == 1000:
    print(str(t.name) + ": " + str(t.weights))
  for t in range(len(threads)//2+1):
    threads[t] = threads[len(threads) - 1]
  tempThreads = []
  for i in range(numchildren):
    tempThreads.append(myThread(i, i, 0, len(word)))
    tempThreads[i].copythread(threads[0])
  threads = tempThreads  
  c = "Passwords.txt"
  f = open(c)
  data = f.read()
  words = parse(data)
  
for i in range(numchildren):
  threads.append(myThread(i, i, 0, len(word)))
for i in range(numgenerations):
  main()