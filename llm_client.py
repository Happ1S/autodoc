# llm_client.py

import os
import openai
from typing import List, Optional

class LLMClient:
    def __init__(self,
                 api_key: Optional[str] = None,
                 model: str = "gpt-4",
                 endpoint: str = "https://api.openai.com/v1"):
        """
        :param api_key: Ваш OpenAI API key. Если не передан, будет взят из OPENAI_API_KEY.
        :param model: модель, например "gpt-4" или "gpt-4-0613"
        :param endpoint: базовый URL OpenAI API.
        """
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Не задан OPENAI_API_KEY")
        openai.api_key = self.api_key
        openai.api_base = endpoint.rstrip('/')
        self.model = model

    def complete(self,
                 prompt: str,
                 system_prompt: str = "You are an expert software engineer. Explain code snippets clearly.",
                 max_tokens: int = 512,
                 temperature: float = 0.2) -> str:
        """
        Делает одиночный запрос в Chat Completion API v1.0+.
        Возвращает текст ответа.
        """
        resp = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        # Берём содержимое первого выбора
        return resp.choices[0].message.content.strip()

    def batch_complete(self,
                       prompts: List[str],
                       system_prompt: str = "You are an expert software engineer. Explain code snippets clearly.",
                       max_tokens: int = 512,
                       temperature: float = 0.2) -> List[str]:
        """
        Последовательно обходит список промптов.
        """
        results: List[str] = []
        for p in prompts:
            try:
                results.append(self.complete(p, system_prompt, max_tokens, temperature))
            except Exception as e:
                print(f"⚠️ LLM error on prompt: {e}")
                results.append("")
        return results
