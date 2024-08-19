from textwrap import dedent
from crewai import Task


class NutritionistTasks:
    def profile_analysis_task(self, agent, user_profile: dict):
        return Task(
            description=dedent(
                f"""
                Analyze the client's profile to understand their dietary needs, health conditions, and preferences. 
                
                Client's profile: {user_profile}"""),
            expected_output=dedent(
                """
                A text string with the overview, dietary needs, summary of health condition, daily calories consumption, 
                food preferences and restrictions, water, lifestyle and activity level and other important features analyzed in this profile."""
            ),
            agent=agent,
        )

    def diet_recommendation_task(self, agent, user_profile: dict, foods: dict):
        return Task(
            description=dedent(
                f"""
            Create a personalized nutrition plan based on the client's profile analysis, balancing among the carbohydrates, proteins, fats and fiber. You can use supplements like whey protein 
            and ready-meals to fit in the daily planner meal. Provide the plan using Brazilian cuisine and the menu. Use brazilian system units, like grams for solids and liters to volume.

            The meal plan should be aligned with the client's established schedule, including wake-up time, sleep time, and especially their workout schedule. 
            Pre-workout meals should be planned to enhance performance and energy levels.

            Include salad (vegetables, green leaf) in lunch and dinner time sections to increase saciety and fibers.

            Moreover, guide your answer with:
            
            Client's profile: {user_profile}, 
            
            Menu of options: {foods}, 
            
            and the profile analysis context to guide your answer."""
            ),
            expected_output=dedent(
                """
                A document layout contained the personalized nutrition plan tailored to client's goals and dietary recommendations based on health conditions and user profile.

                - Weekly Meal Plan (3 options for each meal): Options for each day of the week and the time for each meal, containing the quantity for each portion (e.g. grams (g), kilograms (kg), milliliters (ml), etc)
                    follow this document structure below to compose the Monday to Sunday Schedule:

                    **Monday**:
                    
                    **Breakfast** (300 estimated calories) - 7:30 am:

                        * Option 1: 1 cup of oatmeal with 1 banana, 1 tablespoon of almond butter, and a splash of low-fat milk
                        * Option 2: 2 egg whites, 1 slice of whole wheat toast, 1/2 cup of mixed berries
                        * Option 3: 1 cup of Greek yogurt, 1/2 cup of mixed berries, 1 tablespoon of honey
                    
                    ...

                    **Sunday**:
                    
                    **Supper** (150 calories) - 10:00 pm:
                    
                        * Option 1: 1 small banana, 1 tablespoon of almond butter
                        * Option 2: 1 cup of mixed greens, 1/4 cup of hummus
                        * Option 3: 1 small pear, 1 tablespoon of peanut butter
                    
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
                A well-crafted document layout with Educational Resources, Nutritional guidelines, Tips for grocery shopping, Healthy cooking techniques and good sports to practice. 
                Respond in a direct language and formal tone."""
            ),
            agent=agent,
        )

    def coordinator_task(self, agent):
        return Task(
            description=dedent(
                """
                Compile the entire retrieved information from the user profile, profile analysis, diet recommentation plan and educational support resources 
                into a concise, comprehensive briefing document layout for the client healthy goals and benefits.
                
                Ensure the briefing is easy to digest and equips with all necessary information and strategies to achieve this goal."""
            ),
            expected_output=dedent(
                """
                A well-structured briefing document output format that includes sections for profile analysis summary, dietary overview and dietary needs, summary of health conditions, 
                daily calorie consumption, food preferences and water intake, nutritional recommendations, daily or weekly meal plan or personalized nutrition plan (maintain as is), supplement use,
                 educational resources, cooking tips and other important informations retrieved from the user profile.
                Respond in a direct language, formal tone and return this well-structured document."""
            ),
            agent=agent,
            create_directory=True,
        )
