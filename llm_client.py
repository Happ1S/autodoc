# llm_client.py

import requests
from typing import List


class LLMClient:
    def __init__(self, base_url: str = "http://localhost:8000/v1", api_key: str = None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def complete(self, prompt: str, model: str = "llama", max_tokens: int = 512) -> str:
        """
        Отправляет запрос к LLM серверу и возвращает сгенерированный текст.
        Предполагаем API совместимый с OpenAI.
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": 0.2,
            "stop": None
        }
        url = f"{self.base_url}/completions"
        resp = self.session.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        # для OpenAI-совместимого API
        completions = data.get("choices") or []
        if not completions:
            return ""
        return completions[0].get("text", "")

    def batch_complete(self, prompts: List[str], model: str = "llama", max_tokens: int = 512) -> List[str]:
        """
        Пакетная обработка промптов: возвращает список ответов.
        """
        return [self.complete(p, model=model, max_tokens=max_tokens) for p in prompts]
