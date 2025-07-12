import logging
from livekit.agents import Agent, AgentConfig
from tools import get_weather, search_web, write_email

# Setup logging
logging.basicConfig(level=logging.INFO)

# Define your agent's configuration
agent_config = AgentConfig(
    name="Neo",
    voice="en_us_001",  # You can change the voice style if needed
    tools=[get_weather, search_web, write_email],
)

# Create the agent
agent = Agent(config=agent_config)

# Run the agent in console mode
if __name__ == "__main__":
    agent.run()