# Dialogflow Greek Language Training Dataset - Setup Guide

## Overview
This template provides a comprehensive starting point for creating a Greek language Dialogflow agent. It includes common intents, entities, and training phrases in Greek, along with example fulfillment code.

## Directory Structure
```
dialogflow-gr-intents-/
├── agent_config/           # Agent configuration files
│   └── agent.json         # Main agent settings
├── intents/               # Intent definitions and training phrases
│   ├── Default_Welcome_Intent.json
│   ├── Default_Fallback_Intent.json
│   ├── Get_Information.json
│   ├── Get_Information_usersays_el.json
│   ├── Goodbye.json
│   └── Goodbye_usersays_el.json
├── entities/              # Entity definitions
│   ├── info-type.json
│   └── info-type_entries_el.json
├── examples/              # Example webhook and fulfillment code
│   ├── webhook_fulfillment.js
│   └── package.json
└── docs/                  # Documentation
    └── SETUP_GUIDE.md
```

## Setup Instructions

### 1. Create a New Dialogflow Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Dialogflow API
4. Go to [Dialogflow Console](https://dialogflow.cloud.google.com/)
5. Create a new agent

### 2. Import the Training Data

#### Method 1: Manual Import via Dialogflow Console
1. In the Dialogflow Console, go to your agent settings
2. Navigate to the "Export and Import" tab
3. Use the "Import from ZIP" option if you have packaged this template
4. Or manually create intents and entities using the JSON files as reference

#### Method 2: Using Dialogflow API
```bash
# Install Google Cloud SDK
# Set up authentication
gcloud auth application-default login

# Use the Dialogflow API to import intents and entities
# (Requires additional scripting - see API documentation)
```

### 3. Configure the Agent
1. Update the `agent_config/agent.json` file with your project details:
   - Replace `"your-project-id"` with your actual Google Cloud project ID
   - Update webhook URL if using fulfillment
   - Adjust timezone and other settings as needed

### 4. Set Up Webhook (Optional)
If you want to use the provided webhook example:

1. Navigate to the `examples/` directory
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the webhook server:
   ```bash
   npm start
   ```
4. Deploy to a hosting service (Google Cloud Functions, Heroku, etc.)
5. Update the webhook URL in your Dialogflow agent settings

### 5. Test Your Agent
1. Use the Dialogflow Console simulator to test your agent
2. Try the following sample phrases:
   - "Γεια σας" (Hello)
   - "Θέλω πληροφορίες για προϊόντα" (I want information about products)
   - "Αντίο" (Goodbye)

## Customization

### Adding New Intents
1. Create a new JSON file in the `intents/` directory
2. Follow the structure of existing intent files
3. Create a corresponding `_usersays_el.json` file for training phrases
4. Update the webhook fulfillment code if needed

### Adding New Entities
1. Create entity definition JSON in the `entities/` directory
2. Create corresponding entries file with Greek synonyms
3. Reference the entity in your intent parameters

### Modifying Training Phrases
1. Edit the `*_usersays_el.json` files
2. Add more variations and synonyms in Greek
3. Use proper parameter annotations for entities

## Best Practices

1. **Use Natural Greek Phrases**: Include common Greek expressions and variations
2. **Parameter Extraction**: Use entities for extracting key information
3. **Context Management**: Use contexts for multi-turn conversations
4. **Fallback Handling**: Provide helpful fallback responses
5. **Testing**: Regularly test with native Greek speakers

## Troubleshooting

### Common Issues
1. **Encoding Issues**: Ensure all files are saved in UTF-8 encoding
2. **JSON Validation**: Validate JSON syntax before importing
3. **Entity Recognition**: Test entity recognition with various Greek phrases
4. **Webhook Errors**: Check webhook logs for fulfillment issues

### Getting Help
- [Dialogflow Documentation](https://cloud.google.com/dialogflow/docs/)
- [Greek Language Support](https://cloud.google.com/dialogflow/docs/reference/language)
- [Best Practices Guide](https://cloud.google.com/dialogflow/docs/best-practices)