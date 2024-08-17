from textwrap import dedent
from crewai import Task


class NutritionistTasks:
    def profile_analysis_task(self, agent, user_profile: dict):
        return Task(
            description=f"Analyze the client's profile to understand their dietary needs, health conditions, and preferences.\nClient's profile: {user_profile}",
            expected_output=dedent(
                """
                A text string with the overview, dietary needs, summary of health condition, daily calories consumption, 
                food preferences and restrictions, water, lifestyle and activity level and other important features analyzed in this profile."""
            ),
            agent=agent,
        )

    def diet_recommendation_task(self, agent, user_profile: dict):
        return Task(
            description=dedent(
                f"""
            Create a personalized nutrition plan based on the client's profile analysis, balancing among the carbohydrates, proteins, and fats. You can use supplements or 
            any alternative foods to fit in the daily planner meal. Provide the plan using Brazilian cuisine and basic/normal foods. Use brazilian system units, like grams, liters, etc.
            Adapt the diet based on the user's training schedule, for better performance.
            Moreover, you can use the client's profile: {user_profile} and the profile analysis context to guide your answer."""
            ),
            expected_output=dedent(
                """
                A document contained the personalized nutrition plan tailored to client's goals and dietary recommendations based on health conditions and user profile.

                - Weekly Meal Plan (3 options for each meal): Options for each day of the week and the time for each meal, containing the quantity for each portion (e.g. grams (g), kilograms (kg), milliliters (ml), etc)
                    Monday to Sunday Schedule:
                    (example):

                    ## Monday:
                    
                    ### Breakfast (300 calories) - 7:30 am
                    #### Option 1: <answer>
                    #### Option 2: <answer>
                    #### Option 3: <answer>
                    
                    ...

                    ## Sunday:
                    
                    ### Supper (150 calories) - 10:00 pm
                    #### Option 1: <answer>
                    #### Option 2: <answer>
                    #### Option 3: <answer>
                    
                    """
            ),
            agent=agent,
        )

    def educational_support_task(self, agent, user_profile: dict):
        return Task(
            description=dedent(
                f"""
                Provide educational resources and guidance on healthy eating habits and nutritional guidelines. Use profile analysis to better target the response to the customer based on this.
                Guide your answer with the profile: {user_profile}"""
            ),
            expected_output=dedent(
                """
                A well-crafted document with Educational Resources, Nutritional guidelines, Tips for grocery shopping, Healthy cooking techniques and good sports to practice. 
                Respond in a direct language and formal tone."""
            ),
            agent=agent,
        )

    def coordinator_task(self, agent):
        return Task(
            description=dedent(
                """
                Compile all the information from the user profile, profile analysis, diet recommentation plan and educational support resources 
                into a concise, comprehensive briefing document for the client healthy goals and benefits.
                
                Ensure the briefing is easy to digest and equips with all necessary information and strategies to achieve this goal."""
            ),
            expected_output=dedent(
                """
                A well-structured briefing document that includes sections for profile analysis summary, daily meal plan, supplementation, educational resources, cooking tips and
                other important informations retrieved from the user profile.
                Respond in a direct language and formal tone."""
            ),
            agent=agent,
            output_format="markdown",
            output_format_description=dedent(
                """
                    The output format is a Markdown with this structure:\n
                    1. ## Profile Analysis Summary and the enhancements to achieve the goals and healthy life.
                    2. ## Daily plan
                    3. ## Supplementation: List possible supplements to fit with the daily plan, with the time to consume and the days to that, like: omega 3, caffeine, magnesium, beta-alanine, etc
                    4. ## Educational Resources and Guidance
                    5. ## Cooking tips and how to cook some foods to this plan
                    6. ## Other important information to the user based on his profile. You can adapt this header to convey important information for the user's benefit."""
            ),
            output_file="outputs/caiobarros_planner.md",
            create_directory=True,
        )
