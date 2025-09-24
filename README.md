# Dialogflow Greek Language Training Dataset Template

A comprehensive template for creating Greek language conversational AI using Google Dialogflow. This repository provides a structured foundation with pre-built intents, entities, and training phrases in Greek, along with example fulfillment code.

## 🚀 Features

- **Pre-built Greek Intents**: Common conversational patterns for Greek language applications
- **Entity Definitions**: Greek language entities with synonyms and variations
- **Training Phrases**: Natural Greek language training examples
- **Webhook Examples**: Sample fulfillment code in Node.js
- **Comprehensive Documentation**: Setup guides and best practices
- **Ready-to-Use**: Structured for immediate Dialogflow import

## 📁 Repository Structure

```
dialogflow-gr-intents-/
├── 📁 agent_config/          # Agent configuration
│   └── agent.json           # Main agent settings
├── 📁 intents/              # Intent definitions
│   ├── Default_Welcome_Intent.json
│   ├── Default_Fallback_Intent.json
│   ├── Get_Information.json & training phrases
│   └── Goodbye.json & training phrases
├── 📁 entities/             # Entity definitions
│   ├── info-type.json
│   └── info-type_entries_el.json
├── 📁 examples/             # Code examples
│   ├── webhook_fulfillment.js
│   └── package.json
└── 📁 docs/                 # Documentation
    ├── SETUP_GUIDE.md
    └── TRAINING_PHRASES.md
```

## 🏁 Quick Start

### 1. Clone this repository
```bash
git clone https://github.com/Sintarta/dialogflow-gr-intents-.git
cd dialogflow-gr-intents-
```

### 2. Create a new Dialogflow agent
1. Go to [Dialogflow Console](https://dialogflow.cloud.google.com/)
2. Create a new project and agent
3. Set the default language to Greek (el)

### 3. Import the training data
Follow the detailed instructions in [docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md) for importing intents and entities.

### 4. Test your agent
Try these sample phrases:
- "Γεια σας" (Hello)
- "Θέλω πληροφορίες για προϊόντα" (I want information about products)
- "Αντίο" (Goodbye)

## 🎯 Included Intents

### Core Intents
- **Default Welcome Intent**: Greeting responses in Greek
- **Default Fallback Intent**: Fallback responses when intent isn't recognized
- **Get Information**: Handles information requests with entity extraction
- **Goodbye**: Farewell responses

### Training Phrases Examples
- Information requests: "Θέλω πληροφορίες για...", "Μπορείς να μου πεις για..."
- Greetings: "Γεια σας", "Καλημέρα", "Χαίρετε"
- Farewells: "Αντίο", "Γεια σας", "Καλή συνέχεια"

## 🏷️ Entity Definitions

### info-type Entity
Includes common information categories with Greek synonyms:
- **προϊόντα** (products): προϊόντα, είδη, αγαθά
- **υπηρεσίες** (services): υπηρεσίες, εξυπηρέτηση, παροχές
- **τιμές** (prices): τιμές, κόστος, αξία, τιμολόγιο
- **διαθεσιμότητα** (availability): διαθεσιμότητα, απόθεμα, στοκ
- **ωράριο** (schedule): ωράριο, ώρες λειτουργίας, πρόγραμμα

## 🔧 Webhook Integration

The `examples/` directory contains a complete Node.js webhook example:

```javascript
// Handle Greek language responses
function handleInformationRequest(infoType) {
  const responses = {
    'προϊόντα': 'Διαθέτουμε μεγάλη ποικιλία προϊόντων υψηλής ποιότητας.',
    'υπηρεσίες': 'Προσφέρουμε εξειδικευμένες υπηρεσίες για όλες τις ανάγκες σας.',
    // ... more responses
  };
  return responses[infoType] || 'Δυστυχώς δεν έχω πληροφορίες για αυτό που ζητάτε.';
}
```

## 📖 Documentation

- **[Setup Guide](docs/SETUP_GUIDE.md)**: Complete setup and configuration instructions
- **[Training Phrases Guide](docs/TRAINING_PHRASES.md)**: Best practices for Greek language training phrases

## 🎨 Customization

### Adding New Intents
1. Create intent JSON files following the existing structure
2. Add corresponding training phrases in Greek
3. Update webhook fulfillment if needed

### Extending Entities
1. Add new entity definitions in the `entities/` directory
2. Include Greek synonyms and variations
3. Reference in intent parameters

## 🌍 Language Support

This template is specifically designed for:
- **Primary Language**: Greek (el)
- **Secondary Language**: English (en) - for fallback
- **Locale**: Europe/Athens timezone
- **Character Encoding**: UTF-8

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements (new intents, entities, or training phrases)
4. Test with native Greek speakers
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Documentation**: Check the [docs/](docs/) directory for detailed guides
- **Dialogflow Help**: [Official Dialogflow Documentation](https://cloud.google.com/dialogflow/docs/)

## 🏆 Acknowledgments

Created as a template for Greek language Dialogflow development. Contributions and improvements are welcome from the Greek developer community.

---

**Ready to build your Greek language conversational AI?** Start with this template and customize it for your specific use case!
