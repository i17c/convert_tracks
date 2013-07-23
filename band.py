class Band:
	def __init__(self, collection):
		self.collection = collection
		
	def add(self, name):
		if self.collection.find_one({'name': name}) is None:
			self.collection.insert({'band': name, 'inserted': datetime.datetime.utcnow()})
		
	def delete(self, name):
		self.collection.remove({'name': name}).remove()

	def update(self, name):
		self.collection.update({'name': name}, {'$set': {'name': name, 'modified': datetime.datetime.utcnow()}})