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

    
    def extract_entities(self, text: str) -> dict:
        """
        Extrai entidades nomeadas do texto e organiza por tipo.
        """
    
        entities = {
            "persons": [],
            "organizations": [],
            "locations": []
        }

        results = self.ner_pipeline(text)

        for entity in results:
            label = entity["entity_group"]
            word = entity["word"]

            if label == "PER":
                entities["persons"].append(word)
            
            elif label == "ORG":
                entities["organizations"].append(word)
            
            elif label == "LOC":
                entities["locations"].append(word)
        
        return entities
    




