from crewai import Crew, Process

from agents import NutritionistAgents
from tasks import NutritionistTasks
from inputs import inputs

agents = NutritionistAgents()
tasks = NutritionistTasks()

# Agents
profile_analysis_agent = agents.profile_analysis_agent()
diet_recommendation_agent = agents.diet_recommendation_agent()
educational_support_agent = agents.educational_support_agent()
nutritionist_coordinator_agent = agents.nutritionist_coordinator_agent()

# Tasks
profile_analysis_task = tasks.profile_analysis_task(
    profile_analysis_agent, user_profile=inputs["user_profile"]
)
diet_recommendation_task = tasks.diet_recommendation_task(
    diet_recommendation_agent, user_profile=inputs["user_profile"], foods=inputs["foods"]
)
educational_support_task = tasks.educational_support_task(
    educational_support_agent, user_profile=inputs["user_profile"]
)
coordinator_task = tasks.coordinator_task(nutritionist_coordinator_agent)

diet_recommendation_task.context = [profile_analysis_task]
educational_support_task.context = [profile_analysis_task]
coordinator_task.context = [
    profile_analysis_task,
    diet_recommendation_task,
    educational_support_task,
]

crew = Crew(
    agents=[
        profile_analysis_agent,
        diet_recommendation_agent,
        educational_support_agent,
        nutritionist_coordinator_agent
    ],
    tasks=[
        profile_analysis_task,
        diet_recommendation_task,
        educational_support_task,
        coordinator_task
    ],
)

# Kickoff the Crew
result = crew.kickoff()

print("############")
print(result)
