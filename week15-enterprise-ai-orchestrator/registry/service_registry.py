from services.search_service import SearchService
from services.summarizer_service import SummarizerService
from services.translator_service import TranslatorService
from services.classifier_service import ClassifierService


class ServiceRegistry:

    search = SearchService()

    summarizer = SummarizerService()

    translator = TranslatorService()

    classifier = ClassifierService()