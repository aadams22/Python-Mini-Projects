
#Ashleigh Adams
#adams869
#Python Project


class Random:
	def __init__(self,seed):
		self.seed = seed
		self.n = self.seed
	def next(self):
		self.n = (16807 * self.n) % 2147483647 #Park-Miller algorithm: 7^5=16807, 2^31-1=214783647
		return self.n
	def choose(self, objects):
		return objects[self.next()%len(objects)]



class Grammar:
	def __init__(self, seed):
		self.rand = Random(seed)
		self.rules = {} 

	def rule(self, left, right):
		if left not in self.rules:
			self.rules[left] = [right]
		else:
			self.rules[left].append(right)

	def generate(self):
		s = 'Start'
		if s in self.rules:
			return self.generating((s,))
		else:
			raise RuntimeError('Well shucks! Turns out there is no Start rule!')	

	def generating(self, strings):
		result = '' #the empty string
		for e in strings:
			if e not in self.rules:
				result += (e + ' ')
			else:
				result += self.generating(self.rand.choose(self.rules[e]))
		return result


G = Grammar(101)  
G.rule('Noun',   ('cat',))                                #  01  
G.rule('Noun',   ('boy',))                                #  02  
G.rule('Noun',   ('dog',))                                #  03  
G.rule('Noun',   ('girl',))                               #  04  
G.rule('Verb',   ('bit',))                                #  05  
G.rule('Verb',   ('chased',))                             #  06  
G.rule('Verb',   ('kissed',))                             #  07  
G.rule('Phrase', ('the', 'Noun', 'Verb', 'the', 'Noun'))  #  08  
G.rule('Story',  ('Phrase',))                             #  09  
G.rule('Story',  ('Phrase', 'and', 'Story'))              #  10  
G.rule('Start',  ('Story', '.'))                          #  11

print G.generate()
