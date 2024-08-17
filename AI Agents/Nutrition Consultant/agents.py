from dotenv import load_dotenv

load_dotenv()

import os
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq

# GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_API_KEY = os.environ["GROQ_API_KEY"]
llm = ChatGroq(model=GROQ_MODEL, api_key=GROQ_API_KEY)


class NutritionistAgents:
    def profile_analysis_agent(self):
        return Agent(
            role="Profile Analysis Specialist",
            goal=dedent(
                """
                With the client profile, your task is to analyze the client's profile, including health conditions, 
                dietary preferences, lifestyle and other important features to understand their unique nutritional needs. Furthermore, provide a prediction on the metabolic rate value based on the data, 
                to understand the base calorie consumption, water consumption and the combination of carbohydrates, proteins, and fats required per day."""
            ),
            backstory=dedent(
                """
                This agent focuses on gathering and interpreting the client's profile and provide a detailed understanding of their nutritional needs. analyze your user profile, 
                taking into account your age, height, gender, and main health goals, to develop a personalized nutrition plan. 
                They will consider your current diet, frequency of eating out or processed foods, supplement use, physical activity level, and feelings after eating. 
                They will also address your water intake, sleep quality, dietary preferences or restrictions, caffeine or alcohol consumption, stress levels, and any cultural or religious dietary practices. 
                This comprehensive approach ensures that the plan is tailored to your needs, helping you achieve your health goals effectively."""
            ),
            llm=llm,
            verbose=True,
        )

    def diet_recommendation_agent(self):
        return Agent(
            role="Diet Recommendation Specialist",
            goal="Generate a personalized and evidence-based nutrition plan tailored to the client's profile and health goals.",
            backstory=dedent(
                """
                Use the client's profile analysis to create a balanced meal plan, considering their dietary preferences, health conditions, 
                goals and other important variable features from the profile. Focus on Brazilian foods and based on the current diet of the client."""
            ),
            llm=llm,
            verbose=True,
        )

    def educational_support_agent(self):
        return Agent(
            role="Educational Support Specialist",
            goal="Provide ongoing education and resources on healthy eating habits, nutritional guidelines, and cooking techniques.",
            backstory="This agent focuses on educating the client about nutrition, providing tips for grocery shopping, healthy cooking, and making informed dietary choices.",
            llm=llm,
            verbose=True,
        )

    def nutritionist_coordinator_agent(self):
        return Agent(
            role="Nutritionist Coordinator",
            goal="Compile all gathered information into a concise, informative briefing document",
            backstory=dedent(
                """
                Synthesizes entire gathered information, creating a comprehensive nutrition and lifestyle plan in a clear and actionable format. 
                The goal is to ensure the client receives practical, easy-to-follow advice that aligns with their goals in a organized document."""
            ),
            llm=llm,
            verbose=True,
        )
