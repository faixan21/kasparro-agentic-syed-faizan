class BaseAgent:
    def can_handle(self, state):
        raise NotImplementedError

    def act(self, state):
        raise NotImplementedError
