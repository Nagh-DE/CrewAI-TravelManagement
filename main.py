from crewai import Crew

# get agents and tasks
from agents import agency_manager, local_travel_agent, transport_accomodation_agent
from tasks import travels_recommendations, local_places, transport_accomodation


def init_crew(from_place, to_place, travel_date):
    crew = Crew(
        agents=[agency_manager, local_travel_agent,
                transport_accomodation_agent],
        tasks=[
            travels_recommendations(
                agency_manager, from_place, to_place, travel_date),
            local_places(local_travel_agent, to_place, travel_date),
            transport_accomodation(
                transport_accomodation_agent, from_place, to_place, travel_date)
        ]
        verbose=True
    )
    return crew.kickoff()


from_place = input("Enter from place: ")
to_place = input("Enter to place: ")
travel_date = input("Enter date of travel: ")
print("Here is the report", init_crew(from_place, to_place, travel_date))
