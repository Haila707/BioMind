from app.agents.laboratory_agent import LaboratoryAgent
from app.agents.research_agent import ResearchAgent
from app.agents.healthcare_agent import HealthcareAgent

from app.services.selector import Selector
from app.services.merger import Merger


class Orchestrator:

    def __init__(self):
        self.laboratory = LaboratoryAgent()
        self.research = ResearchAgent()
        self.healthcare = HealthcareAgent()

        self.selector = Selector()
        self.merger = Merger()

    def run(self, request: str):

        selected_agents = self.selector.select_agents(request)

        responses = []

        laboratory_result = None
        research_result = None

        # Laboratory
        if "Laboratory Agent" in selected_agents:
            laboratory_result = self.laboratory.process(request)
            responses.append(laboratory_result)

        # Research
        if "Research Agent" in selected_agents:
            research_result = self.research.process(
                request=request,
                laboratory_result=laboratory_result
            )
            responses.append(research_result)

        # Healthcare
        if "Healthcare Agent" in selected_agents:
            healthcare_result = self.healthcare.process(
                request=request,
                laboratory_result=laboratory_result,
                research_result=research_result
            )
            responses.append(healthcare_result)

        return self.merger.merge(
            request=request,
            responses=responses
        )