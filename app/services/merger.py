from app.services.report_builder import ReportBuilder


class Merger:

    def __init__(self):
        self.report_builder = ReportBuilder()

    def merge(self, request: str, responses: list):

        report = self.report_builder.build(
            request=request,
            responses=responses
        )

        return report