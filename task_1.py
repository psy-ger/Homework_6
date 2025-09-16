class ReverseFileIterator:
	"""
	Клас-ітератор для зворотного читання файлу рядок за рядком.
	"""
	def __init__(self, filename, encoding='utf-8'):
		"""
		Ініціалізує ітератор для зворотного читання файлу.
        
		Args:
			filename (str): Шлях до файлу.
			encoding (str): Кодування файлу.
		"""
		self.filename = filename
		self.encoding = encoding
		self.file = open(filename, 'rb')
		self.file.seek(0, 2)
		self.position = self.file.tell()
		self.buffer = b''

	def __iter__(self):
		"""
		Повертає ітератор (самого себе).
		Returns:
			ReverseFileIterator: Ітератор.
		"""
		return self

	def __next__(self):
		"""
		Повертає наступний рядок з файлу у зворотному порядку.

		Raises:
			StopIteration: Якщо досягнуто початку файлу і всі рядки прочитані.

		Returns:
			str: Наступний рядок з файлу (з кінця до початку).
		"""
		if self.position == 0 and not self.buffer:
			self.file.close()
			raise StopIteration
		while True:
			if b'\n' in self.buffer:
				last_newline = self.buffer.rfind(b'\n')
				line = self.buffer[last_newline+1:]
				self.buffer = self.buffer[:last_newline]
				return line.decode(self.encoding)
			if self.position == 0:
				line = self.buffer
				self.buffer = b''
				return line.decode(self.encoding)
			read_size = min(4096, self.position)
			self.position -= read_size
			self.file.seek(self.position)
			chunk = self.file.read(read_size)
			self.buffer = chunk + self.buffer


def main():
	"""
	Демонструє використання ReverseFileIterator для зворотного читання файлу.
	"""
	filename = "example.txt"
	for line in ReverseFileIterator(filename):
		print(line.rstrip())


if __name__ == "__main__":
	main()
