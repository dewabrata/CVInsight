import json
from anthropic import Anthropic

from app.services.cv_processor_services.base_service import BaseService
from app.utils.prompt import prompt


class ClaudeService(BaseService):
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.client = Anthropic(api_key=f"{api_key}")

    def _call_api(self, text: str) -> dict:
        """
        Calls Anthropic Claude model to extract CV details.
        Reference: https://docs.anthropic.com/claude/reference/messages_post
        """
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": f"{prompt}\n\n###pdf content\n{text}"
                    }
                ],
                system="You are a CV parsing assistant.",
                temperature=0
            )
            return json.loads(response.content[0].text.strip())
        except Exception as e:
            raise RuntimeError(f"Anthropic API error: {e}")
