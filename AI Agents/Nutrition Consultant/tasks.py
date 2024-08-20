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
                daily calorie consumption, food preferences and water intake, nutritional recommendations, daily or weekly meal plan or personalized nutrition plan (maintain as is), 
                supplement use, educational resources, cooking tips and other important informations retrieved from the user profile.
                Respond in a direct language, formal tone and return this well-structured document.

                Below there is an example to guide your response's structure:

                ##  Personalized Nutrition and Lifestyle Plan
				
				**1. Client Profile Overview:**

				* **Age:** 26
				* **Height:** 1.80m
				* **Weight:** 90kg
				* **Body Fat Percentage:** 26%
				* **Activity Level:** Highly active (5 days/week high-intensity weightlifting)
				* **Goals:** Weight loss, reduce body fat percentage, target abdominal fat
				* **Food Preferences:** Wholemeal bread, eggs, bananas, rice, chicken, beans, beetroot, yogurt, whey protein, strawberries, powdered milk, sliced turkey breast
                * **Dietary Preferences:**  No specific preferences or restrictions.
                * **Hydration:** You drink 4 liters of water daily, which is excellent!
                * **Supplements:** You use caffeine (200mg daily), whey protein, omega 3 and creatine.
					
				**2. Profile Analysis**

				* The client is relatively active, going to the gym 5 times a week and pushing high lifts at a median level.
				* The client's diet is relatively balanced, but may benefit from increasing protein intake and reducing carbohydrate intake from sources like wholemeal bread and rice.
				* The client's water intake is approximately 2 liters per day, which is relatively low.
				* The client's sleep quality and duration are relatively poor, ranging from 6-8 hours per day.

				**3. Dietary Overview and Dietary Needs**

				* Daily calorie consumption: 2500-2800 calories
				* Macronutrient breakdown:
						+ Carbohydrates: 250-300g
						+ Protein: 170-200g
						+ Fat: 70-80g
				* Meal frequency: 5-6 meals per day
				* Hydration: At least 3-4 liters of water per day

				**4. Summary of Health Conditions**

				* The client does not have any medical conditions or food allergies.
				* However, the client may be at risk for developing conditions like insulin resistance and cardiovascular disease due to high body fat percentage and abdominal fat.

				**5. Daily Calorie Consumption**

				* The client's daily calorie consumption is estimated to be around 2500-2800 calories.
				* This is relatively high, but necessary to support muscle growth and maintenance.

				**6. Food Preferences and Restrictions**

				* The client does not have any food preferences or restrictions.
				* However, the client may benefit from reducing intake of processed foods like sliced turkey breast and increasing intake of whole, nutrient-dense foods.

				**7. Water Intake**

				* The client's water intake is approximately 2 liters per day, which is relatively low.
				* It is recommended that the client increase water intake to at least 3-4 liters per day to support muscle growth and maintenance.

				**8. Lifestyle and Activity Level**

				* The client is relatively active, going to the gym 5 times a week and pushing high lifts at a median level.
				* However, the client may benefit from increasing physical activity level and incorporating more cardio exercises into routine.

				**9. Other Important Features**

				* The client's sleep quality and duration are relatively poor, ranging from 6-8 hours per day.
				* It is recommended that the client aim for 7-9 hours of sleep per night to support muscle growth and recovery.

				**10. Nutritional Recommendations**

				* Increase protein intake to 1.6-2.2g/kg body weight per day
				* Reduce carbohydrate intake from sources like wholemeal bread and rice
				* Increase water intake to at least 3-4 liters per day
				* Aim for 7-9 hours of sleep per night
				* Incorporate stress-reducing activities into daily routine, such as meditation or yoga
				* Increase physical activity level and incorporate more cardio exercises into routine

                **11. Weekly Meal Plan:**

				**Monday:**

				* **Breakfast (350 estimated calories) - 7:30 am:**
					* Option 1: 1 cup of cooked oatmeal with 1/2 banana, 1 tablespoon of chia seeds, and a splash of skim milk.
					* Option 2: 2 eggs scrambled with 1/4 cup chopped vegetables (tomato, onion, peppers) and 1 slice of whole wheat toast.
					* Option 3: 1 cup of Greek yogurt with 1/2 cup mixed berries, 1 tablespoon of chopped nuts (walnuts, almonds).
				* **Pre-workout (200 estimated calories) - 11:30 am:**
					* Option 1: 1 cup of cottage cheese with 1/4 cup of pineapple chunks.
					* Option 2: 2 bananas with 1 tablespoon of peanut butter.
					* Option 3: 1 whole wheat wrap filled with 1/2 cup shredded chicken, lettuce, and 1 tablespoon of avocado.
				* **Lunch (400 estimated calories) - 1:00 pm:**
					* Option 1: 100g cooked brown rice, 100g grilled chicken breast, 100g cooked beans, 150g mixed green salad with 1 tablespoon olive oil and lemon juice dressing.
					* Option 2: 100g tapioca flour with 100g shredded chicken, 100g cooked beans, 150g mixed greens salad with 1 tablespoon olive oil and lemon juice dressing.
					* Option 3: 100g quinoa with 100g grilled tilapia, 100g cooked lentils, 150g mixed greens salad with 1 tablespoon olive oil and lemon juice dressing.
				* **Afternoon Snack (150 estimated calories) - 4:00 pm:**
					* Option 1: 1 cup of sliced fruits (apple, banana, papaya) with 1 tablespoon of cinnamon powder.
					* Option 2: 150g low-fat yogurt with 1/4 cup of granola and berries.
					* Option 3: 1 small handful of mixed nuts (cashews, almonds, walnuts).
				* **Dinner (450 estimated calories) - 7:00 pm:**
					* Option 1: 100g grilled chicken breast with 100g sweet potato puree, 100g steamed broccoli, and 1 tablespoon of olive oil.
					* Option 2: 100g baked cod with 100g brown rice, 100g cooked lentils, and 150g mixed greens salad with 1 tablespoon olive oil and lemon juice dressing.
					* Option 3: 100g ground beef stir-fried with 100g mixed vegetables (carrots, peppers, onions) served with 100g brown rice and 150g mixed greens salad.
				* **Supper (150 calories) - 9:30 pm:**
					* Option 1: 1 small banana with 1 tablespoon of almond butter.
					* Option 2: 1 small cup of herbal tea with 1/2 cup of berries.
					* Option 3: 1 small pear with 1 tablespoon of peanut butter.

                **Tuesday - Sunday:**  Follow the same meal structure as Monday, varying the options within each category to create different combinations.

                **12.  Additional Tips**

                * Drink at least 3-4 liters of water per day
				* Incorporate stress-reducing activities into daily routine, such as meditation or yoga
				* Aim for 7-9 hours of sleep per night
				* Increase physical activity level and incorporate more cardio exercises into routine
				* Reduce carbohydrate intake from sources like wholemeal bread and rice
				* Increase protein intake to 1.6-2.2g/kg body weight per day
			
				Remember, achieving your goals requires consistency, dedication, and a balanced approach to nutrition and lifestyle. Celebrate your progress and stay motivated!
				
				**So now, let's begin!**
                
                """
            ),
            agent=agent,
            create_directory=True,
        )
