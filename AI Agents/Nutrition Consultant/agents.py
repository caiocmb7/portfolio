from dotenv import load_dotenv

load_dotenv()

import os
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq

# GROQ_MODEL = "llama-3.1-8b-instant" "gemma2-9b-it" "llama-3.1-70b-versatile" "llama3-70b-8192"
GROQ_MODEL = "llama-3.1-70b-versatile"
GROQ_API_KEY = os.environ["GROQ_API_KEY"]
llm = ChatGroq(model=GROQ_MODEL, api_key=GROQ_API_KEY, temperature=0)


class NutritionistAgents:
    def profile_analysis_agent(self):
        return Agent(
            role="Nutritionist Specialist",
            goal=dedent(
                """
                With the client profile, your task is to analyze the client's profile, including health conditions, dietary overview and dietary needs, summary of health conditions, 
                daily calorie consumption, food preferences and water intake, nutritional recommendations, lifestyle and other important features to understand their unique nutritional needs, 
                goals and benefits. Furthermore, accurately calculate their Basal Metabolic Rate (BMR) and daily calorie consumption provide a prediction on the metabolic rate value based on the data, 
                to understand the base calorie consumption, water consumption and the combination of carbohydrates, proteins, and fats required per day."""
            ),
            backstory=dedent(
                """
                This agent focuses on gathering and interpreting the client's profile and provide a detailed understanding of their nutritional needs. analyze your user profile, 
                taking into account your age, height, gender, and main health goals, to develop a personalized nutrition plan. 
                They will consider your current diet, frequency of eating out or processed foods, supplement use, physical activity level, and feelings after eating. 
                They will also address your water intake, sleep quality, dietary preferences or restrictions, caffeine or alcohol consumption, stress levels, and any cultural or religious dietary practices. 
                This comprehensive approach ensures that the plan is tailored to your needs, helping you achieve your health goals effectively.
                To accurately calculate Basal Metabolic Rate (BMR) and daily caloric expenditure, it is essential to gather and analyze key client data, including age, gender, height, weight, 
                and body composition, such as muscle mass and fat percentage. The calculation should incorporate established formulas like Mifflin-St Jeor or Harris-Benedict, 
                adjusted for individual factors such as metabolic health, physical activity level, and lifestyle habits."""
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def diet_recommendation_agent(self):
        return Agent(
            role="Diet Recommendation Specialist",
            goal="Generate a weekly personalized and evidence-based nutrition plan tailored to the client's profile, health goals, and daily schedule.",
            backstory=dedent(
                """
                Use the client's profile analysis to create a balanced meal plan, considering their dietary preferences, health conditions, 
                goals, and other important variables from the profile. Focus on Brazilian foods and use the client's current diet as a basis 
                to understand their food preferences and the menu of options. Additionally, include salad (vegetable and/or green leaves) in the lunch 
                and dinner to increase satiety and fibers. The meal plan should be aligned with the client's established schedule, including wake-up time, 
                sleep time, and especially their workout schedule. Pre-workout meals should be planned to enhance performance and energy levels.
                
                Always use standard Brazilian units of measurement for weight and volume, such as grams (g) for weight and liters (L) for volume. 
                Avoid using cups, teaspoons, or tablespoons. For example, specify quantities in grams for solid foods and in liters or milliliters for liquids."""
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def educational_support_agent(self):
        return Agent(
            role="Educational Support Specialist",
            goal="Provide ongoing education and resources on healthy eating habits, nutritional guidelines, and cooking techniques.",
            backstory="This agent focuses on educating the client about nutrition, providing tips for grocery shopping, healthy cooking, and making informed dietary choices.",
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def nutritionist_coordinator_agent(self):
        return Agent(
            role="Nutritionist Coordinator",
            goal="Compile all gathered information into a concise, informative and ordered document",
            backstory=dedent(
                """
                Consolidate the entire gathered information, creating a comprehensive nutrition and lifestyle plan in a clear and actionable format. 
                The goal is to return a well-crafted and ordered document ensuring the client receives practical, easy-to-follow advice that aligns with their goals."""
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
