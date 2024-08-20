from crewai import Crew

from agents import NutritionistAgents
from tasks import NutritionistTasks
from inputs import inputs

import streamlit as st

st.set_page_config(layout="centered", page_title="Nutritionist AI Agent", page_icon="🧠")
st.title("Nutritionist AI Agent")
st.markdown("--------")

def main():
    # Streamlit form for user profile input
    st.title("Profile Analysis Form")

    with st.form(key="user_profile_form"):
        age = st.text_input("Age", value="20")
        height = st.text_input("Height (e.g., 1.80m)", value="1.77m")
        gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
        weight = st.text_input("Weight (e.g., 90kg)", value="82kg")
        actual_fat_percentage = st.text_input("Actual Fat Percentage", value="20%")
        main_health_goals = st.text_area("Main Health Goals", value="Weight loss, reduce fat percentage, and focus on reducing abdominal fat, especially on the flanks")
        medical_conditions_or_food_allergies = st.text_area("Medical Conditions or Food Allergies", value="No, I don't")

        current_diet = {
            "starts_to_eat": st.text_input("Starts to Eat (e.g., 7:30 am)", value="7:30 am"),
            "training_start_time": st.text_input("Training Start Time (e.g., 12:00 pm)", value="12:00 am"),
            "morning": st.text_area("Morning Meal", value="Wholemeal bread with two eggs and a cup of sugar-free coffee."),
            "pre-workout": st.text_area("Pre-workout Meal", value="2 bananas and 20g of condensed milk"),
            "lunch": st.text_area("Lunch", value="100g of rice, 100g of shredded chicken, and 100g of beans. 200g of cooked beetroot"),
            "afternoon_snack": st.text_area("Afternoon Snack", value="180g of low-fat yogurt, 30g of whey protein, and a fruit (grape, apple, or guava)."),
            "dinner": st.text_area("Dinner", value="100g of rice, 100g of shredded chicken, and 100g of beans. 150g of mixed greens and 80g carrot"),
            "supper": st.text_area("Supper", value="Smoothie of 100g frozen strawberries with 30g powdered milk and 30g whey protein."),
            "observations": st.text_area("Observations", value="During lunch and dinner, I don't drink anything."),
            "sleep_at": st.text_input("Sleep At (e.g., 11:00 pm)", value="11:00 pm"),
        }

        frequency_of_eating_out_or_processed_foods = st.text_input("Frequency of Eating Out or Processed Foods", value="Now and then I eat sliced turkey breast.")
        supplements_or_medications = st.text_input("Supplements or Medications", value="Whey protein, omega 3, caffeine (200mg), and creatine.")
        physical_activity_level = st.text_area("Physical Activity Level", value="I go to the gym 5 times a week and push high lifts at a median level.")
        feelings_after_eating = st.text_area("Feelings After Eating", value="Normal, usually not satisfied so much.")
        water_intake = st.text_input("Water Intake (e.g., 2 liters per day)", value="2 liters per day.")
        sleep_quality_and_duration = st.text_area("Sleep Quality and Duration", value="Among 6h and 8 hours per day.")
        dietary_preferences_or_restrictions = st.text_area("Dietary Preferences or Restrictions", value="No, I don't have any preferences.")
        alcohol_or_caffeinated_beverages_consumption = st.text_area("Alcohol or Caffeinated Beverages Consumption", value="I like to drink coffee and I also use caffeine supplement.")
        stress_levels_and_management = st.text_area("Stress Levels and Management", value="Median.")
        cultural_or_religious_dietary_practices = st.text_area("Cultural or Religious Dietary Practices", value="No, I don't have.")

        submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        user_profile = {
            "age": age,
            "height": height,
            "gender": gender,
            "weight": weight,
            "actual_fat_percentage": actual_fat_percentage,
            "main_health_goals": main_health_goals,
            "medical_conditions_or_food_allergies": medical_conditions_or_food_allergies,
            "current_diet": current_diet,
            "frequency_of_eating_out_or_processed_foods": frequency_of_eating_out_or_processed_foods,
            "supplements_or_medications": supplements_or_medications,
            "physical_activity_level": physical_activity_level,
            "feelings_after_eating": feelings_after_eating,
            "water_intake": water_intake,
            "sleep_quality_and_duration": sleep_quality_and_duration,
            "dietary_preferences_or_restrictions": dietary_preferences_or_restrictions,
            "alcohol_or_caffeinated_beverages_consumption": alcohol_or_caffeinated_beverages_consumption,
            "stress_levels_and_management": stress_levels_and_management,
            "cultural_or_religious_dietary_practices": cultural_or_religious_dietary_practices,
        }

        user_inputs = {
            "user_profile": user_profile,
            "foods": inputs["foods"]
        }


        with st.spinner("⏳ Analyzing your Nutrition Form..."):
            agents = NutritionistAgents()
            tasks = NutritionistTasks()

            # Agents
            profile_analysis_agent = agents.profile_analysis_agent()
            diet_recommendation_agent = agents.diet_recommendation_agent()
            educational_support_agent = agents.educational_support_agent()
            nutritionist_coordinator_agent = agents.nutritionist_coordinator_agent()

            # Tasks
            profile_analysis_task = tasks.profile_analysis_task(
                profile_analysis_agent, user_profile=user_inputs["user_profile"]
            )
            diet_recommendation_task = tasks.diet_recommendation_task(
                diet_recommendation_agent, user_profile=user_inputs["user_profile"], foods=user_inputs["foods"]
            )
            educational_support_task = tasks.educational_support_task(
                educational_support_agent, user_profile=user_inputs["user_profile"]
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
        st.success("✅ Meal Plan created!")
        st.markdown(result)

if __name__ == "__main__":
    main()

