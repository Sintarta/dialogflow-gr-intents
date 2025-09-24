# Dialogflow Greek Training Dataset Template - Overview

## 📋 Template Contents

This template provides a complete foundation for building Greek language conversational AI applications with Google Dialogflow.

### ✅ What's Included

#### 🏗️ Core Structure
- **5 Pre-built Intents** with Greek responses
- **1 Entity Definition** with Greek synonyms  
- **20+ Training Phrases** in natural Greek
- **Agent Configuration** optimized for Greek language
- **Webhook Example** with Greek response handling

#### 📁 File Inventory

**Agent Configuration (1 file)**
```
agent_config/agent.json - Complete agent settings
```

**Intents (8 files)**
```
intents/Default_Welcome_Intent.json      - Welcome responses
intents/Default_Fallback_Intent.json     - Fallback handling
intents/Get_Information.json             - Information requests
intents/Get_Information_usersays_el.json - Training phrases
intents/Goodbye.json                     - Farewell responses  
intents/Goodbye_usersays_el.json         - Training phrases
intents/Help.json                        - Help responses
intents/Help_usersays_el.json           - Training phrases
```

**Entities (2 files)**
```
entities/info-type.json                  - Entity definition
entities/info-type_entries_el.json       - Greek entries & synonyms
```

**Examples (3 files)**
```
examples/webhook_fulfillment.js          - Node.js webhook example
examples/package.json                    - Dependencies
examples/import_to_dialogflow.py         - Import script
```

**Documentation (3 files)**
```
docs/SETUP_GUIDE.md                     - Complete setup instructions
docs/TRAINING_PHRASES.md                - Greek language guide
TEMPLATE_OVERVIEW.md                    - This overview
```

### 🎯 Intent Capabilities

| Intent | Purpose | Sample Phrases |
|--------|---------|---------------|
| **Welcome** | Greet users | "Γεια σας", "Καλημέρα" |
| **Information** | Handle requests | "Θέλω πληροφορίες για προϊόντα" |
| **Help** | Provide assistance | "Βοήθεια", "Τι μπορώ να κάνω;" |
| **Goodbye** | End conversations | "Αντίο", "Γεια σας" |
| **Fallback** | Handle unknowns | *Automatic fallback handling* |

### 🏷️ Entity Recognition

**info-type Entity** recognizes:
- προϊόντα (products)
- υπηρεσίες (services) 
- τιμές (prices)
- διαθεσιμότητα (availability)
- ωράριο (schedule)
- επικοινωνία (contact)

Each with multiple Greek synonyms for better recognition.

### 🌍 Language Features

- **Primary Language**: Greek (el)
- **Timezone**: Europe/Athens
- **Character Encoding**: UTF-8
- **Regional Support**: Standard Modern Greek
- **Formality Levels**: Both formal and informal phrases

### 🚀 Getting Started Options

#### Option 1: Manual Import
1. Create new Dialogflow agent
2. Manually create intents using JSON as reference
3. Copy training phrases and responses

#### Option 2: Programmatic Import
1. Use the provided Python import script
2. Set up Google Cloud authentication
3. Run automated import process

#### Option 3: Export/Import
1. Package files into Dialogflow export format
2. Use Dialogflow Console import feature
3. Bulk import entire agent

### 🛠️ Customization Guide

#### Adding New Intents
1. Create JSON file following existing pattern
2. Add corresponding `_usersays_el.json` for training
3. Update webhook fulfillment if needed

#### Extending Entities  
1. Add new entity definition JSON
2. Create entries file with Greek synonyms
3. Reference in intent parameters

#### Modifying Responses
1. Edit response arrays in intent JSON files
2. Add variations for natural conversation
3. Include context-appropriate formality

### 📊 Quality Metrics

- **Intent Coverage**: 5 essential conversation flows
- **Training Diversity**: 4-5 variations per intent
- **Entity Synonyms**: 3-5 synonyms per entity value
- **Language Quality**: Native Greek speaker reviewed
- **Code Quality**: All JSON validated and tested

### 🔧 Technical Requirements

**For Basic Use:**
- Google Cloud Project
- Dialogflow API enabled
- Greek language support

**For Webhook:**
- Node.js runtime
- Express.js framework
- Cloud hosting (optional)

**For Import Script:**
- Python 3.x
- google-cloud-dialogflow library
- Service account credentials

### 📈 Next Steps

1. **Set up** your Dialogflow project
2. **Import** the training data
3. **Test** the basic conversations
4. **Customize** for your specific use case
5. **Deploy** webhook for dynamic responses
6. **Expand** with additional intents and entities

### 🎓 Learning Resources

- [Dialogflow Documentation](https://cloud.google.com/dialogflow/docs/)
- [Greek Language Guide](docs/TRAINING_PHRASES.md)
- [Setup Instructions](docs/SETUP_GUIDE.md)

---

**This template saves hours of initial setup and provides a solid foundation for Greek language conversational AI development.**