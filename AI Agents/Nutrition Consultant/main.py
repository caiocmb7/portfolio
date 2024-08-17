from crewai import Crew

from agents import NutritionistAgents
from tasks import NutritionistTasks

inputs = {
    "user_profile": {
        "age": "26",
        "height": "1.80m",
        "gender": "Male",
        "weight": "90kg",
        "actual_fat_percentage": "26%",
        "main_health_goals": "Weight loss, reduce fat percentage, and focus on reducing abdominal fat, especially on the flanks",
        "medical_conditions_or_food_allergies": "No, I don't",
        "current_diet": {
            "starts_to_eat":"7:30 am",
            "morning": "Wholemeal bread with two eggs and a cup of sugar-free coffee.",
            "lunch": "100g of rice, 100g of shredded chicken, and 100g of beans.",
            "afternoon_snack": "180g of low-fat yogurt, 30g of whey protein, and a fruit (grape, apple, or guava).",
            "dinner": "100g of rice, 100g of shredded chicken, and 100g of beans.",
            "supper": "Smoothie of 100g frozen strawberries with 30g powdered milk and 30g whey protein.",
            "observations": "During lunch and dinner, I don't drink anything.",
            "sleep_at":"11:00 pm",
        },
        "frequency_of_eating_out_or_processed_foods": "Now and then I eat sliced turkey breast.",
        "supplements_or_medications": "Whey protein, omega 3, caffeine (200mg), and creatine.",
        "physical_activity_level": "I go to the gym 5 times a week and push high lifts at a median level.",
        "feelings_after_eating": "Normal, usually not satisfied so much.",
        "water_intake": "I need to perform better to this. I would say 2 liters per day.",
        "sleep_quality_and_duration": "Among 6h and 8 hours per day.",
        "dietary_preferences_or_restrictions": "No, I don't have any preferences.",
        "alcohol_or_caffeinated_beverages_consumption": "I like to drink coffee and I also use caffeine supplement.",
        "stress_levels_and_management": "Median.",
        "cultural_or_religious_dietary_practices": "No, I don't have.",
    }
}

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
    diet_recommendation_agent, user_profile=inputs["user_profile"]
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

# crew = Crew(
#     agents=[
#         profile_analysis_agent,
#         diet_recommendation_agent,
#         educational_support_agent,
#         nutritionist_coordinator_agent,
#     ],
#     tasks=[
#         profile_analysis_task,
#         diet_recommendation_task,
#         educational_support_task,
#         coordinator_task,
#     ],
# )

crew = Crew(
    agents=[
        profile_analysis_agent,
        diet_recommendation_agent,
    ],
    tasks=[
        profile_analysis_task,
        diet_recommendation_task,
    ],
)

# Kickoff the Crew
result = crew.kickoff()

print("############")
print(result)
