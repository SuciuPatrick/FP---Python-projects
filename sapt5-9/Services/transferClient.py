class TransferClient:
	def __init__(self, client, days):
		self._client = client
		self._days = days

	@property
	def client(self):
		return self._client

	@property
	def days(self):
		return self._days

	def __str__(self):
		return str(self._days) + " " * (30 - len(str(self._days))) + str(self._client)