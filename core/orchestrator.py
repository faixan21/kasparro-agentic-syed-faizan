class Orchestrator:
    def __init__(self, agents):
        self.agents = agents

    def run(self, state):
        while True:
            progress = False

            for agent in self.agents:
                if agent.can_handle(state):
                    state = agent.act(state)
                    progress = True

            if not progress:
                break

        return state
