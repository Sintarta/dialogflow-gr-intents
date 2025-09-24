#!/usr/bin/env python3
"""
Script to help import the training dataset to Dialogflow using the API.
Requires google-cloud-dialogflow library.

Install: pip install google-cloud-dialogflow
"""

import json
import os
from google.cloud import dialogflow

def import_intents(project_id, language_code='el'):
    """Import intents from JSON files to Dialogflow."""
    client = dialogflow.IntentsClient()
    parent = f"projects/{project_id}/agent"
    
    intents_dir = "../intents"
    
    for filename in os.listdir(intents_dir):
        if filename.endswith(".json") and not filename.endswith("_usersays_el.json"):
            intent_path = os.path.join(intents_dir, filename)
            training_phrases_path = intent_path.replace(".json", "_usersays_el.json")
            
            print(f"Processing intent: {filename}")
            
            with open(intent_path, 'r', encoding='utf-8') as f:
                intent_data = json.load(f)
            
            # Create Dialogflow intent object
            intent = dialogflow.Intent()
            intent.display_name = intent_data['name']
            
            # Add training phrases if they exist
            if os.path.exists(training_phrases_path):
                with open(training_phrases_path, 'r', encoding='utf-8') as f:
                    training_data = json.load(f)
                
                for phrase_data in training_data:
                    training_phrase = dialogflow.Intent.TrainingPhrase()
                    for part in phrase_data['data']:
                        phrase_part = dialogflow.Intent.TrainingPhrase.Part()
                        phrase_part.text = part['text']
                        if 'alias' in part:
                            phrase_part.entity_type = part['meta']
                            phrase_part.alias = part['alias']
                        training_phrase.parts.append(phrase_part)
                    intent.training_phrases.append(training_phrase)
            
            # Add responses
            for response in intent_data['responses']:
                for message in response['messages']:
                    if message['type'] == '0':  # Text response
                        text_message = dialogflow.Intent.Message()
                        text_message.text.text.extend(message['speech'])
                        intent.messages.append(text_message)
            
            # Create the intent
            try:
                response = client.create_intent(
                    request={"parent": parent, "intent": intent, "language_code": language_code}
                )
                print(f"Created intent: {response.display_name}")
            except Exception as e:
                print(f"Error creating intent {intent_data['name']}: {str(e)}")

def import_entities(project_id, language_code='el'):
    """Import entities from JSON files to Dialogflow."""
    client = dialogflow.EntityTypesClient()
    parent = f"projects/{project_id}/agent"
    
    entities_dir = "../entities"
    
    for filename in os.listdir(entities_dir):
        if filename.endswith(".json") and not filename.endswith("_entries_el.json"):
            entity_path = os.path.join(entities_dir, filename)
            entries_path = entity_path.replace(".json", "_entries_el.json")
            
            print(f"Processing entity: {filename}")
            
            with open(entity_path, 'r', encoding='utf-8') as f:
                entity_data = json.load(f)
            
            # Create Dialogflow entity type object
            entity_type = dialogflow.EntityType()
            entity_type.display_name = entity_data['name']
            entity_type.kind = dialogflow.EntityType.Kind.KIND_MAP
            
            # Add entries if they exist
            if os.path.exists(entries_path):
                with open(entries_path, 'r', encoding='utf-8') as f:
                    entries_data = json.load(f)
                
                for entry in entries_data:
                    entity_entry = dialogflow.EntityType.Entity()
                    entity_entry.value = entry['value']
                    entity_entry.synonyms.extend(entry['synonyms'])
                    entity_type.entities.append(entity_entry)
            
            # Create the entity type
            try:
                response = client.create_entity_type(
                    request={"parent": parent, "entity_type": entity_type, "language_code": language_code}
                )
                print(f"Created entity type: {response.display_name}")
            except Exception as e:
                print(f"Error creating entity {entity_data['name']}: {str(e)}")

if __name__ == "__main__":
    # Replace with your Google Cloud Project ID
    PROJECT_ID = "your-project-id"
    
    print("Starting import process...")
    print("Make sure you have set up authentication:")
    print("export GOOGLE_APPLICATION_CREDENTIALS='path/to/your/service-account-key.json'")
    print()
    
    # Import entities first (intents may depend on them)
    print("Importing entities...")
    import_entities(PROJECT_ID)
    
    print("\nImporting intents...")
    import_intents(PROJECT_ID)
    
    print("\nImport completed!")
    print("Please verify the import in the Dialogflow Console.")