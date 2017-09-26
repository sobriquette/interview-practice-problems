# Imagine you have a call center with three levels of employees: respondent,
# manager, and director. An incoming telephone call must be first allocatedto a
# respondent who is free. If the respondent can't handle the call, he or she must
# escalate the call to a manager. If the manager is not free or not able to handle it,
# then the call should be escalatedto adirector. Design the classes and datastructures for this problem. Implement a method dispatchCall() which assigns a
# call to the first available employee.
from Queue import Queue

class Employee:
	def __init__(self, name, level, is_available=True):
		self.name = name
		self.level = level
		self.is_available = is_available

	def get_name(self):
		return self.name

	def get_level(self):
		return self.level

	def get_availability(self):
		return self.is_available

class Respondent(Employee):
	def __init__(self, manager=None):
		self.manager = manager
		self.calls = []

	def get_manager(self):
		return self.manager

	def escalate_call(self):
		return self.get_manager

	def reset_availability(self, completed):
		if completed:
			self.is_available = True

class Manager(Employee):
	def __init__(self, director=None):
		self.director = director
		self.respondents = {}

	def get_director(self):
		return self.director

	def get_respondents(self):
		return self.respondents

	def add_respondent(self, respondent):
		if respondent.manager is None:
			# update the respondent's manager to this one
			respondent.manager = self.get_name

			if respondent.name not in respondents:
				respondents[respondent.name] = respondent
		else:
			raise Exception("This employee already has a manager: {}".format(respondent.manager))

	def escalate_call(self):
		return self.director

	def reset_availability(self, completed):
		if completed:
			self.is_available = True

class Director(Employee):
	def __init__(self):
		self.managers = {}

	def get_managers(self):
		return self.managers

	def add_managers(self, manager):
		if manager.director is None:
			if manager.director is None:
				# update manager's director to this one
				manager.director = self.get_name

class CallCenter:
	def __init__(self):
		self.employees = {
			'respondents': [],
			'managers': [],
			'directors': []
		}
		self.incoming_calls = Queue()

	def add_calls_to_waiting_list(self, call):
		self.incoming_calls.enqueue(call)

	def search_for_availability(self, employee_type):
		e = 0
		while not self.employees[employee_type][e].is_available and \
			  e < len(self.employees[employee_type]):
				e += 1
		return e

	def dispatch_call(self):
		"""
			Assigns respondents to calls in the queue
			type: None
			return type: Respondent
		"""
		while not self.incoming_calls.isEmpty():
			call = self.incoming_calls.dequeue()

			# find a respondent who is available
			avbl_respondent = self.search_for_availability(self, 'respondents')

			# case: no respondents are available
			# dispatch to first available manager
			if avbl_respondent == len(self.employees['respondents']):
				avbl_manager == self.search_for_availability(self, 'managers')
				
				# case: no managers are available
				# dispatch to first available director
				if avbl_manager == len(self.employees['directors']):
					avbl_director = self.search_for_availability('directors')

				# case: we found an available manager
				# assign their availability to False
				else:
					self.employees['managers'][avbl_manager].is_available = False
					self.employees['managers'][avbl_manager].calls.append(call)

			# case: we found an available respondent
			# assign their availability to False
			else:
				self.employees['respondents'][avbl_respondent].is_available = False
				self.employees['respondents'][avbl_respondent].calls.append(call)

