import random
import asyncio

tasks_map = {}

def create_id():
  return random.randint(0, 1_000_000)

async def some_task(string):
  await asyncio.sleep(2)
  return random.randint(0, 10)

def make_and_return():
  task_id = create_id()
  tasks_map[task_id] = None
  task = asyncio.create_task(some_task())
  task.add_done_callback(create_print_on_success(task_id))
  return task_id

def create_print_on_success(task_id):
  def print_on_success(task):
    result = task.result()
    tasks_map[task_id] = result
  
  return print_on_success

async def main():
  id = make_and_return()
  while True:
    if id in tasks_map and tasks_map[id] is None:
      await asyncio.sleep(0.5)
      print(f'task {id} is not finished')
      continue
    print('task_id', id)
    print(tasks_map[id])
    id = make_and_return()

asyncio.run(main())

