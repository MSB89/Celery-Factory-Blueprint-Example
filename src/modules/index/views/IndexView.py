from flask.views import MethodView

from src.tasks.example_task import example_task


class IndexView(MethodView):

    def get(self):
        example_task.apply_async()
        return 'Task Created'
