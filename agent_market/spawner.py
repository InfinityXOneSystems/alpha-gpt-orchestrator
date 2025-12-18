from agent_market.agent import ElasticAgent

ACTIVE_AGENTS = []

def spawn(role, objective):
    agent_id = f\"agent-{len(ACTIVE_AGENTS)+1}\"
    agent = ElasticAgent(agent_id, role, objective)
    ACTIVE_AGENTS.append(agent)
    agent.start()
    return agent_id

def list_agents():
    return [a.agent_id for a in ACTIVE_AGENTS]
