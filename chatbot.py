import json
import sys
import os
import subprocess as sp

class Eon():
    def __init__(self, name):
        try:
            memory = open(name + '.json', 'r')
        except FileNotFoundError:
            memory = open(name + '.json', 'w')
            memory.write('[["Éon"], {"oi": "Olá! Qual seu nome?", "tchau": "Tchau! Tchau!"}]')
            memory.close()
            memory = open(name+'.json', 'r')
        self.name = name
        self.known, self.phrases = json.load(memory)
        memory.close()
        self.historic = [None]

    def listen(self, phrase=None):
        return phrase.lower()

    def think(self, phrase):
        if phrase in self.phrases:
            return self.phrases[phrase]
        if phrase == 'aprende':
            return 'O que você quer que eu aprenda?'
        if phrase == 'dicionário de japonês':
            return "http://nihongo.monash.edu/cgi-bin/wwwjdic?1C"
        
        # historic
        lastPhrase = self.historic[-1]
        if lastPhrase == 'Olá! Qual seu nome?':
            name = self.getName(phrase)
            response = self.answerName(name)
            return response

        if lastPhrase == 'O que você quer que eu aprenda?':
            self.key = phrase
            return 'Digite o que eu devo responder:'
        if lastPhrase == 'Digite o que eu devo responder:':
            response = phrase
            self.phrases[self.key] = response
            self.saveMemory()
            return 'Aprendido!'
        try:
            response = str(eval(phrase))
            return response
        except:
            pass
        return 'Não entendi...'

    def getName(self, name):
        if 'meu nome é ' in name:
            name = name[11:]
        name = name.title()
        return name

    def answerName(self, name):
        if name in self.known:
            if name != 'Éon':
                phrase = 'Eaew, '
            else:
                phrase = 'Não acredito, uma xará '
        else:
            phrase = 'Muito prazer, '
            self.known.append(name)
            self.saveMemory()
        return phrase + name + '!'

    def saveMemory(self):
        memory = open(self.name + '.json', 'w')
        json.dump([self.known, self.phrases], memory)
        memory.close()

    def speak(self, phrase):
        if 'Executa ' in phrase:
            platform = sys.platform
            command = phrase.replace('Executa ', '')
            if 'win' in platform:
                os.startfile(command)
            if 'linux' in platform:
                try:
                    sp.Popen(command)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', command])
        else:
            print(phrase)
        self.historic.append(phrase)