import os.path

class Converter:
	code = {}

	def __init__(self, codeFile):
		self._loadCodeFile(codeFile)

	def _loadCodeFile(self, codeFile):
		if not os.path.isfile(codeFile):
			raise IOError("Code file at '%s' not found." % codeFile)
		for line in file(codeFile):
			tmp = line.split(":")
			self.code[tmp[0]] = tmp[1]

	def toMorse(self, text):
		result = ""
		for c in text.upper():
			if c in self.code:
				result += str(self.code[c])
		return result.strip()

	def toText(self, morse):
		raise NotImplementedError("toText not yet implemented.")