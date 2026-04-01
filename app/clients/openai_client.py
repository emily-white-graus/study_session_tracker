from openai import OpenAI, OpenAIError

class StudySummaryClient:
    def __init__(self, api_key: str, model: str) -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate_summary(self, prompt: str) -> str:
        try:
            response = self.client.responses.create(model=self.model, input=prompt)
        except OpenAIError as exc:
            raise RuntimeError(f"OpenAI request failed: {exc}") from exc

        if not response.output_text:
            raise RuntimeError("OpenAI returned an empty summary.")

        return response.output_text.strip()
