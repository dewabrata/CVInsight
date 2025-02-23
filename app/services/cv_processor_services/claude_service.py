import json
from anthropic import Anthropic

from app.services.cv_processor_services.base_service import BaseService
from app.utils.prompt import prompt


class ClaudeService(BaseService):
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.client = Anthropic(api_key=f"{api_key}")

    def _call_api(self, text: str, is_analysis: bool = False, **kwargs) -> dict:
        """
        Calls Anthropic Claude model to extract CV details or analyze CV.
        Reference: https://docs.anthropic.com/claude/reference/messages_post
        """
        try:
            system_message = "You are a CV analysis expert." if is_analysis else "You are a CV parsing assistant."
            content = text if is_analysis else f"{prompt}\n\n###pdf content\n{text}"
            
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                system=system_message,
                temperature=0
            )
            
            # Parse the response and ensure it's valid JSON
            try:
                result = json.loads(response.content[0].text.strip())
                return result
            except json.JSONDecodeError:
                # If JSON parsing fails, try to extract JSON from the response
                text_response = response.content[0].text.strip()
                json_start = text_response.find('{')
                json_end = text_response.rfind('}') + 1
                if json_start >= 0 and json_end > json_start:
                    json_str = text_response[json_start:json_end]
                    return json.loads(json_str)
                raise RuntimeError("Failed to parse JSON response from Claude")
        except Exception as e:
            raise RuntimeError(f"Anthropic API error: {e}")
