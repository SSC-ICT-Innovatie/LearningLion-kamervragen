import os
import re

class Preprocessor:
  
	def run_preprocessing(self, text:str, functions: list) -> str:
			"""
			Run all preprocessing functions on the text.
			"""
			for function in functions:
					text = function(text)
			return text

	def merge_hyphenated_words(self, text: str) -> str:
			"""
			Merge words in the text that have been split with a hyphen.
			"""
			return re.sub(r"(\w)-\n(\w)", r"\1\2", text)

	def fix_newlines(self, text: str) -> str:
			"""
			Replace single newline characters in the text with spaces.
			"""
			return re.sub(r"(?<!\n)\n(?!\n)", " ", text)

	def remove_multiple_newlines(self, text: str) -> str:
			"""
			Reduce multiple newline characters in the text to a single newline.
			"""
			return re.sub(r"\n{2,}", "\n", text)

	def strip_file_path(self, file_path: str) -> str:
			"""
			Strips the file path to the filename
			"""
			return os.path.basename(file_path)

	def extract_footnotes(self, text:str):
			"""
				haal de tekst op die in de voetnoten staat
   		"""
			footnotePattern = re.compile(r'(\d+)\s+(.*?)(?=\d+\s|$)', re.DOTALL)

			strings_with_numbers = []
			footnotes = []
			matches = list(footnotePattern.finditer(text))
			for match in matches:
					footnote_number = match.group(1)
					footnote_text = match.group(2).strip()
					strings_with_numbers.append(footnote_number)
					strings_with_numbers.append(footnote_text)
			footnote_index = 0
			pages = []
			current_page = []
			pattern = re.compile(r'\b' + str(footnote_index + 1) + r'\b')
			for string in strings_with_numbers:
					if string is None:
							continue
					if '’s-Gravenhage' in string:
							pages.append(current_page)
							current_page = []
					else:
							current_page.append(string)
			for page in pages:
					page.reverse()
					passedItems = []
					foundfooternotes = False
					for pageitem in page:
							if foundfooternotes:
									passedItems.reverse()
									for passeditem in passedItems:
											pattern = re.compile(r'\b' + str(footnote_index + 1) + r'(?![\d])')

											if pattern.search(passeditem):  # Checks if the exact number is in the string
													footnotes.append(passeditem)
													footnote_index += 1
											else:
													if("ah-tk" in passeditem):
															break
													if footnotes[len(footnotes) - 1].endswith("-"):
															footnotes[len(footnotes) - 1] = f"{footnotes[len(footnotes) - 1]}{passeditem.strip()}".strip()
													else:
															footnotes[len(footnotes) - 1] = f"{footnotes[len(footnotes) - 1]} {passeditem.strip()}".strip()

									break
							if pattern.search(pageitem):  # Checks if the exact number is in the string
									footnote_index += 1
									footnotes.append(pageitem)
									foundfooternotes = True
							else:
									passedItems.append(pageitem)

			return footnotes

	def get_footer(self, text):
			"""
			Haal de voettekst op
			"""

			splitted = text.split(" ")
			footer = []
			splitted.reverse()
			if splitted[0].isdigit():
					splitted.pop(0) # Remove page number
			for split in splitted:
					if "Tweede" in split:
							footer.append(split)
							footer.reverse()
							return " ".join(footer)
					else:
							footer.append(split)
			return ""

	def get_question_number(self,text):
		"""
			Haal de vraagnummers op
		"""
		vraagnumber_pattern = r"Vraag (\d+(?:[ ,]en[ ,]\d+)*)" #TODO: add support for comma seperated numbers
		vraagnumbers = re.findall(vraagnumber_pattern, text)
		return vraagnumbers
	def get_footnote_number(self,text):
		"""
			Haal de voetnootnummers op
		"""
		footnotenumber_pattern = r"(\d+)"
		footnotenumbers = re.findall(footnotenumber_pattern, text)
		return footnotenumbers[0]


	def get_question_and_answer(self, text):
					"""
					Haal de vragen en antwoorden op
					"""
					# footer = self.get_footer(text)
					# pages = self.get_amount_of_pages(text,footer)
					# text = self.remove_footer_and_pagenumbers(text,footer,pages)
					# docspecs = self.get_doc_specs(text)
					# text = text.replace(docspecs, "")
					# text = self.normalize_whitespace(text)
					# question_pattern = r"(Vraag\s\d+.*?)(?=\s*Antwoord)"
					# answer_pattern = r"(Antwoord\s\d+.*?)(?=Vraag|\Z)"
					question_pattern = r'(?<=\n\n)Vraag(?:en)?\s+\d+(?:\s+en\s+\d+)*[^\n]*(?:\n(?!\n).*)*' #regex patterns for matching
					answer_pattern = r'(?<=\n\n)Antwoord(?:en)?\s+\d+(?:\s+en\s+\d+)*[^\n]*(?:\n(?!\n).*)*'

					questions = re.findall(question_pattern, text)
					answers = re.findall(answer_pattern, text)

					questions = [q.strip() for q in questions]
					answers = [a.strip() for a in answers]

					# questions = [self.normalize_whitespace(q) for q in questions]
					# answers = [self.normalize_whitespace(a) for a in answers]

					return [questions, answers]
        
	def get_context(self,text):
			"""
				haal de inleiding op
   		"""
			# Pattern to find the first multi-digit number (1 or more digits) and everything up to the first question
			pattern = re.compile(r'\s*((?:(?!Vraag\s\d).)*?)(Vraag\s\d)', re.DOTALL)
			match = pattern.search(text)

			if match:
					# Return the text between the number and the first question
					result = match.group(1).strip()
					return result
			else:
					return None
				
	def remove_footnotes(self, text, footnotes):
			"""
			Haal de voetnoten uit de tekst
			"""
			for footnote in footnotes:
					text = text.replace(footnote, "")
			return text.strip()

	def get_amount_of_pages(self, text, footer):
			"""
			Haal het aantal pagina's op
   		"""
			return text.find(footer)

	def remove_footer(self, text, footer):
			"""
				Verwijder de voettekst
			"""
			if footer is not None:
					text = text.replace(footer, "")
					return text.strip()
			return text.strip()

	def remove_footer_and_pagenumbers(self, text,footer, amountpages):
			"""
				Verwijder de voettekst en paginanummers
			"""
			textLength = len(text)
			for number in range(amountpages):
					text = self.remove_footer(text, f"{footer} {str(number + 1)}")
			if(textLength == len(text)):
					for number in range(amountpages):
							text = self.remove_footer(text, footer)
			return text.strip()

	def get_doc_specs(self, text):
			"""
				Haal de document specificaties op
			"""
			pattern = r"(ah-tk-\d{8}-\d{3} ISSN\s*\d{4}\s*-\s*\d{4}\s*’s-Gravenhage\s*\d{4})"

			match = re.search(pattern, text)

			if match:
					return match.group(1)
			else:
					return "Desired identifiers not found."

	def normalize_whitespace(self, text):
			"""
			normaaliseer de whitespace
			"""
			# Replace multiple spaces with a single space
			return re.sub(r'\s+', ' ', text).strip()
	
	def get_heading(self,text):
		"""
			Haal de kop op
		"""
		result = re.search(r'^(.*?)(?=Vraag 1)', text, re.DOTALL)

		heading = result.group(1).replace("#", "").replace("*", "").strip()
		cleaned_heading = re.sub(r'^\s*\d+\s*$', '', heading, flags=re.MULTILINE).strip()
		return cleaned_heading
	def get_footnotes(self,text):
		"""
			haal de voetnoten op
   	"""
		footnote_pattern = r'(?m)^\d+\s+.*'
		footnotes = re.findall(footnote_pattern, text)
		firstFootNoteNumber = 1
		actual_footnotes = []
		for footnote in footnotes:
			if footnote.startswith(f"{firstFootNoteNumber} ") and not footnote[len(f"{firstFootNoteNumber} "):].startswith("\n"):
					actual_footnotes.append(footnote)
					firstFootNoteNumber += 1
		return actual_footnotes
	def clean_text_MD(self, text):
		"""
		Maak de tekst schoon
		"""
		# Remove metadata
		text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
		# Remove empty lines
		text = re.sub(r'\n\s*\n', '\n', text)
		# Remove leading and trailing whitespace
		text = text.strip()
		# remove makrdown
		text = re.sub(r'\[.*?\]\(.*?\)', '', text)
		# remove page seperators
		text = re.sub(r'--', '', text)
		# remove headings
		text = re.sub(r'^#+\s*', '', text)
		# remove list items
		text = re.sub(r'^\s*-\s*', '', text)
		# remove bold
		text = re.sub(r'\*\*', '', text)
		# remove italic
		text = re.sub(r'\*', '', text)
		# remove links
		text = re.sub(r'\[.*?\]\(.*?\)', '', text)
		# Remove multiple spaces
		text = re.sub(r'\s+', ' ', text)
		# Remove leading and trailing whitespace
		text = text.strip()
		# Remove leading and trailing newlines
		text = text.strip('\n')
  
		return text
   