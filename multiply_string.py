import random
import asyncio

tasks_map = {}

def create_id():
  return random.randint(0, 1_000_000)

async def string_task(string):
  await asyncio.sleep(15)
  return string * 10

def create_print_on_success(task_id):
  def print_on_success(task):
    result = task.result()
    tasks_map[task_id] = result
  
  return print_on_success

def create_task(string):
  task_id = create_id()
  tasks_map[task_id] = None
  task = asyncio.create_task(string_task(string))
  task.add_done_callback(create_print_on_success(task_id))
  return task_id

def get_task_if_finished(task_id):
  if (task_id in tasks_map and tasks_map[task_id] is not None):
    return tasks_map[task_id]

  return 'not_ready'



