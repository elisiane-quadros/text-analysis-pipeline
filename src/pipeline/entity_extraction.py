from transformers import pipeline

class EntityExtractor:
    def __init__(self):
        """
        Inicializa o modelo de Named Entity Recognition (NER).
        Esse modelo será usado para identificar pessoas, organizações e locais em um texto.
        """
        self.ner_pipeline = pipeline(
            task="ner",
            model="dbmdz/bert-large-cased-finetuned-conll03-english",
            aggregation_strategy="simple"
        )

    def _clean_word(self, word: str) -> str:
        """Remove artefatos de tokenização remanescentes."""
        return word.replace("##", "").strip()
    
    def extract_entities(self, text: str) -> dict:
        """
        Extrai entidades nomeadas do texto e organiza por tipo.
        """
        results = self.ner_pipeline(text)

        entities = {
            "persons": set(),
            "organizations": set(),
            "locations": set()
        }

        """
        Mapeamento de labels do modelo para nossos nomes amigáveis
        """
        label_map = {
            "PER": "persons",
            "ORG": "organizations",
            "LOC": "locations"
        }

        for ent in results:
            label = ent["entity_group"]
            if label in label_map:
                clean_name = self._clean_word(ent["word"])
                if len(clean_name) > 1: # Ignora caracteres isolados
                    entities[label_map[label]].add(clean_name)
        
        """
        Converte de volta para lista para ser serializável em JSON
        """
        return {k: list(v) for k, v in entities.items()}
    




