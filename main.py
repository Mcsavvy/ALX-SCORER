"""
This programs aims to implement a close to perfect imitation of 
ALX scoring algorithm. It implements a task class, uses to represent tasks.
A task has a few attributes

* name - name of the given task
* worth - the number of points this task is worth
* mandatory - is the task mandatory? True/False
* score - the number of points earned
* before_first - was the task completed before the first deadline? True/False
* before_second - was the task completed before the second deadline? True/False

NOTE: If before_false and before_second is False, this program assumes that the task was completed after the second deadline
"""


from dataclasses import dataclass
from operator import attrgetter
from itertools import chain

@dataclass
class task:
	name: str
	worth: int
	score: int
	mandatory: bool = True
	before_first: bool = False
	before_second: bool = False
	

@dataclass
class task_set:
	all: "list[task]"
	
	@property
	def before_first(self) -> "tuple[task]":
		if not hasattr(self, "_bf"):
			l = []
			for task in self.all:
				if task.before_first:
					l.append(task)
			self._bf = tuple(l)
		return self._bf
		
	@property
	def before_second(self) -> "tuple[task]":
		if not hasattr(self, "_bs"):
			l = []
			for task in self.all:
				if task.before_second:
					l.append(task)
			self._bs = tuple(l)
		return self._bs
		
	@property
	def after_second(self) -> "tuple[task]":
		if not hasattr(self, "_as"):
			l = []
			for task in self.all:
				if not (self.before_first or self.before_second):
					l.append(task)
			self._as = tuple(l)
		return self._as
		
	@property
	def worth(self) -> int:
		return sum(map(attrgetter('worth'), self.all))
		
	@property
	def before_first_score(self) -> float:
		return sum(map(attrgetter("score"), self.before_first))
		
	@property
	def before_second_score(self) -> float:
		return sum(map(attrgetter("score"), self.before_second))

	@property	
	def after_second_score(self) -> float:
		return sum(map(attrgetter("score"), self.after_second))
		
	@property
	def score(self) -> float:
		return (self.before_first_score / self.worth) + (
			   (self.before_second_score / self.worth) * 0.65) + (
			   (self.after_second_score / self.worth) * 0.5)
			

def score(tasks: "list[task]"):
	# separate the tasks
	mandatory_tasks = task_set([task for task in tasks if task.mandatory])
	optional_tasks = task_set([task for task in tasks if not task.mandatory])
	total = mandatory_tasks.score + (mandatory_tasks.score * optional_tasks.score)
	print(f"Out Of {len(tasks)} task[s] completed:")
	print(f"* {len(mandatory_tasks.before_first)} mandatory task[s] were completed before the first deadline")
	print(f"* {len(mandatory_tasks.before_second)} mandatory task[s] were completed before the second deadline")
	print(f"* {len(mandatory_tasks.after_second)} mandatory task[s] were completed after the second deadline")
	print(f"* {len(optional_tasks.before_first)} optional task[s] were completed before the first deadline")
	print(f"* {len(optional_tasks.before_second)} optional task[s] were completed before the second deadline")
	print(f"* {len(optional_tasks.after_second)} optional task[s] were completed after the second deadline")
	print('-' * 20)
	print(f"+ IN MANDATORY TASKS, YOU SCORED {mandatory_tasks.score*100:.2f}% of {mandatory_tasks.worth}")
	print(f"+ IN OPTIONAL TASKS, YOU SCORED {optional_tasks.score*100:.2f}% of {optional_tasks.worth}")
	print(f"+ TOTAL SCORE: {total*100:10.2f}%")
	
			
	


