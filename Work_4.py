def replaceWithAsterisk(sent,word):
  return sent.replace(word, "*" * len(word))
sent = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
censored_sent = replaceWithAsterisk(sent, "zapret.txt")
print(censored_sent)
