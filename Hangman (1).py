import random

class Hangman:
  def __init__(self,word,chance,index=None):
    """
    Initialize all the variables needed
    for the program.

    """
    self.word = word
    self.chance = chance
    self.index = index
    self.flag = False
    self.length = len(self.word)
    self.display = self.length * '#'
    self.total_char = []
    self.freq = {}
    self.used_char = []
    self.find_var_index = []

  def display_word(self):
    """
    Display the anonymized word.
    """

    len_word = len(self.word)
    len_round = round(0.3*len_word)
    print("Welcome to the Hangman Game!!!\n")
    print(f"There are {len_word} letters in the word. You have to guess {len_word-len_round} letters.\n")
    self.index = random.sample(range(0,len_word),len_round)
    print("The anonymized word is:")
    for i in range(0,len_word):
      if i in self.index:
        print(self.word[i],end=' ')
      else:
        print(self.display[i],end=' ')
    for i in range(0,len_word):
      if i in self.index:
        char = self.word[i]
        self.total_char.append(char)

  def get_freq(self):
    """
    Builds a dictionary which contain the 
    word as key and it's frequency as value
    """
    unique_word = set(self.word)
    for i in unique_word:
      count = self.word.count(i)
      if count == 1:
        continue
      self.freq[i] = count

  def char_position(self,word,char):
    """
    Take input word and character and
    returns the index of the character.
    """
    position = []
    for i in range(len(word)):
      if word[i] == char:
        position.append(i)
    return position

  def play(self):
    """
    Main function which takes the input from 
    the players.
    * Checks if the letter is correct or not.
    * If correct display then checks if occurs multiple times or not.
    * Checks if all words are correct or not.
    * Display the word if successful in predicting the word.
    * Otherwise ends when you reach the limit. 
    """
    count = 0
    for i in range(0,self.chance):
      count_guessed = 0
      guessed_char = input("\nEnter the letter you guessed:\n")
      if guessed_char in self.word:
        if (guessed_char in self.used_char):
          print("You have already used this letter.")
          continue
        self.used_char.append(guessed_char)   
        find_var = self.char_position(self.word,guessed_char)
        print(find_var)
        for i in range(0,self.length):
          if i in find_var:
            print(f"The character in index {i} is {self.word[i]}")
            self.total_char.append(self.word[i])
            self.find_var_index.append(i)
        for i in range(0,self.length):
          if i in self.find_var_index or i in self.index:
            print(self.word[i],end=' ')
          else: 
            print(self.display[i],end=' ')
      else:
        print("You couldn't guess the correct word!!!")
        count += 1
        self.used_char.append(guessed_char)
        if (count == 5):
          print("You couldn't complete the game!!!")
          break
                
      for i in range(0,self.length):
        if self.word[i] in self.total_char:
          count_guessed += 1
          if count_guessed == self.length and all([self.freq[i] <= self.total_char.count(i) for i in self.freq.keys()]):
            print("\nYOU WON!!!")
            print("You have correctly guessed the word!!!")
            self.flag = True
    
      if self.flag:
        break

if __name__ == '__main__':
  word = input("Enter the word to guess:")
  hang = Hangman(word,10)
  hang.display_word()
  hang.get_freq()
  hang.play()