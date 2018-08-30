from locust import HttpLocust, TaskSet, task
import json

class SampleTasks(TaskSet):

  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
  user_id = None

  def on_start(self):
    self.login()

  def login(self):
    body = json.dumps({'email': 'hoge', 'pass': 'hoge'})
    response = self.client.post(
      '/login',
      body,
      headers = self.headers
    )
    json_response_dict = response.json()
    self.user_id = json_response_dict['user_id']

  def greet(self):
    body = json.dumps({'user_id': self.user_id})
    self.client.post(
      '/greet',
      body,
      headers = self.headers
    )

  @task
  def scenario(self):
    self.greet()

class SampleBehavior(HttpLocust):
  task_set = SampleTasks
  min_wait = 100
  max_wait = 200
