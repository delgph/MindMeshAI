from typing import List

import dotenv
from crewai import Crew, Process, Agent, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task

from agents.sentiment import Sentimental_tool

dotenv.load_dotenv()


@CrewBase
class Sentiment():
    """Sentiment Crew"""

    #agents_config = "config/agents.yaml"
    #tasks_config = "config/tasks.yaml"
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def observe_a(self) -> Agent:
        return Agent(
            config=self.agents_config["observe_a"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )
    @agent
    def sentimental_a(self) -> Agent:
        return Agent(
            config=self.agents_config["sentimental_a"],
            tools=[Sentimental_tool()],
            allow_delegation=False,
            verbose=True,
        )
    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config["summarizer"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def observe_task(self) -> Task:
        return Task(
            config=self.tasks_config["observe_task"],
            agent=self.observe_a(),
            #output_json=mental_h,
            output_file="mental.json",
        )

    @task
    def sentiment_task(self) -> Task:
        return Task(
            config=self.tasks_config["sentiment_task"],
            agent=self.sentimental_a(),
        )

    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config["summarize_task"],
            agent=self.summarizer(),
            output_file="output.md",
        )
    @crew
    def crew(self) -> Crew:
        """Creates sentimental analyzer crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

    def run(self, inputs=None):
        """Run the crew
        
        Args:
            inputs (dict, optional): Input parameters for the crew
        """
        if inputs is None:
            inputs = {
                "text": "Im feeling depressed and Im not happy",
                "user":"Diana",
                "days":"12 days"
            }
            
        return self.crew().kickoff(inputs=inputs)