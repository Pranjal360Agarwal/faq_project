from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

LANGUAGES = [("en", "English"), ("hi", "Hindi"), ("bn", "Bengali")]


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    language = models.CharField(max_length=2, choices=LANGUAGES, default="en")

    def get_translation(self, lang):
        cache_key = f"faq_{self.id}_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        translation = FAQ.objects.filter(id=self.id, language=lang).first()

        if not translation:
            translated_question = translator.translate(self.question, dest=lang).text
            translated_answer = translator.translate(self.answer, dest=lang).text
            translation = FAQ.objects.create(
                question=translated_question, answer=translated_answer, language=lang
            )

        cache.set(cache_key, {"question": translation.question, "answer": translation.answer}, timeout=86400)
        return {"question": translation.question, "answer": translation.answer}

    def __str__(self):
        return f"{self.language} - {self.question[:50]}"
