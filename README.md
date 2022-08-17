# ALX-SCORER
A Simple Implementation Of The ALX Scoring Algorithm

## Tasks

This program provides a `task` class for creating tasks, just like project tasks.
Tasks can be optional or mandatory. Each task can also be completed before the first deadline, before the second deadline or after the second deadline.
The total score is calculate using these conditions.

### Usage

In case of a project with 4 tasks, 3 of which are mandatory and each 10 points and one is optional(advanced) for 10 points. Finished the first two tasks before the first deadline, finished third task before second deadline, finished the last optional task after the second deadline. What would my score be?

```python
# import "tasks" and "score"
from main import task, score

#create  a list of tasks
tasks = [
    task(name="Task 1", worth=10, mandatory=True, score=10, before_first=True),
    task(name="Task 2", worth=10, mandatory=True, score=10, before_first=True),
    task(name="Task 3", worth=10, mandatory=True, score=10, before_second=True),
    task(name="Task 4", worth=10, mandatory=False, score=10)
]

# score it
score(tasks)
```

```
Out Of 4 task[s] completed:
* 2 mandatory task[s] were completed before the first deadline
* 1 mandatory task[s] were completed before the second deadline
* 0 mandatory task[s] were completed after the second deadline
* 0 optional task[s] were completed before the first deadline
* 0 optional task[s] were completed before the second deadline
* 1 optional task[s] were completed after the second deadline
--------------------
+ IN MANDATORY TASKS, YOU SCORED 88.33% of 30
+ IN OPTIONAL TASKS, YOU SCORED 50.00% of 10
+ TOTAL SCORE:     132.50%


```

> This code should run as is!