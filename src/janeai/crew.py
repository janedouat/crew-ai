from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.custom_tool import HackerNewsTool, HackerNewsSearchTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Janeai():
    """Janeai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def hackernews_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['hackernews_researcher'], # type: ignore[index]
            tools=[HackerNewsTool(), HackerNewsSearchTool()],
            verbose=True
        )

    @agent
    def hackernews_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['hackernews_analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def jane_digital_twin_light(self) -> Agent:
        return Agent(
            config=self.agents_config['jane_digital_twin_light'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def fetch_personalized_stories_task(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_personalized_stories_task'], # type: ignore[index]
        )

    @task
    def create_tldr_summaries_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_tldr_summaries_task'], # type: ignore[index]
            output_file='hackernews_tldr_summaries.md'
        )

    @task
    def conversational_intro_task(self) -> Task:
        return Task(
            config=self.tasks_config['conversational_intro_task'], # type: ignore[index]
            output_file='jane_digital_twin_intro.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Janeai crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
