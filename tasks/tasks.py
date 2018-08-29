from locust import HttpLocust, TaskSet, task

class ElbTasks(TaskSet):
  @task
  def status(self):
      self.client.get("/")

class ElbWarmer(HttpLocust):
  task_set = ElbTasks
  min_wait = 1
  max_wait = 2
