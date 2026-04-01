from openai import OpenAI, OpenAIError

# talks to openai api
class StudySummaryClient:
    def __init__(self, api_key: str, model: str) -> None:
        #creates openai client
        self.client = OpenAI(api_key=api_key)
        # stores chosen model
        self.model = model

    def generate_summary(self, prompt: str) -> str:
        # sends prompt to openai
        try:
            response = self.client.responses.create(model=self.model, input=prompt)
        except OpenAIError as exc:
            # turns errors into app errors
            raise RuntimeError(f"OpenAI request failed: {exc}") from exc

        if not response.output_text:
            #handles blank ai replies
            raise RuntimeError("OpenAI returned an empty summary.")

        #clean summary text
        return response.output_text.strip()
