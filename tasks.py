from crewai import Task
from textwrap import dedent
from agents import azure_llm

from datetime import date


def travels_recommendations(agent, from_place, to_place, travel_date):
    return Task(
        description=f"""
            Collect and summarize all details about travel for user from {from_place} to {to_place}

            Pay special attention to any significant events, happening in {to_place} around this date {travel_date}
    
            Your final answer MUST be a report that includes a
            comprehensive summary of the latest best deals.
            Make sure to use the most recent data as possible.
        """,
        agent=agent,
        llm=azure_llm,
        expected_output='report of summary of tourist spots based on user requirements'
    )


def local_places(agent, to_place, travel_date):
    return Task(description=f"""
            Extract all the best tourist spots in {to_place}, based on the weather or season.
            try to include few vendor details like car travels, bike rentals in local.

            Pay special attention to any significant events, happening in {to_place} around this date {travel_date}
    
            Your final answer MUST be a report that includes a
            comprehensive summary of the latest events happening or places a user can visit without any problem.
            Make sure to use the most recent data as possible.
        """,
                agent=agent,
                llm=azure_llm,
                expected_output='report of all required details for a user while travelling to new places for vacation, make sure the cost you provide are in Rupees'
                )


def transport_accomodation(agent, from_place, to_place, travel_date):
    return Task(description=f"""
            Extract all the best deals for transport details in all modes like flights or trains from {from_place} to {to_place}.
            and also get best accomodation details in {to_place} with rating above 4 stars around this date {travel_date}
    
            Your final answer MUST be a report that includes a
            comprehensive summary of the transport details and acoomodation details
            Make sure to use the most recent data as possible.
        """,
                agent=agent,
                llm=azure_llm,
                expected_output='report of best deals for travel and accomodation as per user requirements, make sure the cost you provide are in Rupees'
                )
