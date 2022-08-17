"""
This programs aims to implement a close to perfect imitation of 
ALX scoring algorithm. It implements a task class, uses to represent tasks.
A task has a few attributes

* name - name of the given task
* worth - the number of points this task is worth
* mandatory - is the task mandatory? True/False
* earned - the number of points earned
* fininshed_before_first_deadline - was the task completed before the first deadline? True/False

"""


from dataclasses import dataclass
from operator import attrgetter
from itertools import chain

@dataclass
class task:
	name: str
	worth: int
	mandatory: bool
	earned: int
	before_first: bool = False
	before_second: bool = False
	
def score(tasks: "list[task]"):
	# separate the tasks
	mandatory_tasks: "dict[str, list[task]]" = {
		"all": [],
		"before_first": [],
		"before_second": [],
		"after_second": []
	}
	optional_tasks: "dict[str, list[task]]" = {
		"all": [],
		"before_first": [],
		"before_second": [],
		"after_second": []
	}
	M = mandatory_tasks
	O = optional_tasks
	for task in tasks:
		if task.mandatory:
			M['all'].append(task)
			if task.before_first:
				M['before_first'].append(task)
			elif task.before_second:
				M['before_second'].append(task)
			else:
				M['after_second'].append(task)
		else:
			O['all'].append(task)
			if task.before_first:
				O['before_first'].append(task)
			elif task.before_second:
				O['before_second'].append(task)
			else:
				O['after_second'].append(task)
	M.update({
		"total": sum(
 			map(attrgetter("worth"), M['all'])
		),
		"before_first_deadline_total": sum(
			map(attrgetter("earned"), M['before_first'])
		),
		"before_second_deadline_total": sum(
			map(attrgetter("earned"), M['before_second'])
		),
		"after_second_deadline_total": sum(
			map(attrgetter("earned"), M['after_second'])
		)
	})
	M["score"] = (M['before_first_deadline_total'] / M['total']) + (
		(M['before_second_deadline_total'] / M['total']) * 0.65) + (
		(M['after_second_deadline_total'] / M['total']) * 0.50)
	O.update({
		"total": sum(
 			map(attrgetter("worth"), O['all'])
		),
		"before_first_deadline_total": sum(
			map(attrgetter("earned"), O['before_first'])
		),
		"before_second_deadline_total": sum(
			map(attrgetter("earned"), O['before_second'])
		),
		"after_second_deadline_total": sum(
			map(attrgetter("earned"), O['after_second'])
		)
	})
	O["score"] = (O['before_first_deadline_total'] / O['total']) + (
		(O['before_second_deadline_total'] / O['total']) * 0.65) + (
		(O['after_second_deadline_total'] / O['total']) * 0.50)
	
	total = M["score"] + (M["score"] * O["score"])
	print(f"Out Of {len(tasks)} task[s] completed:")
	print(f"* {len(M['before_first'])} mandatory task[s] were completed before the first deadline")
	print(f"* {len(M['before_second'])} mandatory task[s] were completed before the second deadline")
	print(f"* {len(M['after_second'])} mandatory task[s] were completed after the second deadline")
	print(f"* {len(O['before_first'])} optional task[s] were completed before the first deadline")
	print(f"* {len(O['before_second'])} optional task[s] were completed before the second deadline")
	print(f"* {len(O['after_second'])} optional task[s] were completed after the second deadline")
	print('-' * 20)
	print(f"+ IN MANDATORY TASKS, YOU SCORED {M['score']*100:.2f}% of {M['total']}")
	print(f"+ IN OPTIONAL TASKS, YOU SCORED {O['score']*100:.2f}% of {O['total']}")
	print(f"+ TOTAL SCORE: {total*100:10.2f}%")
	
			
	


