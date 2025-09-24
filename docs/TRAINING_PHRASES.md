# Greek Training Phrases Guide

## Overview
This guide provides examples and best practices for creating effective training phrases in Greek for your Dialogflow agent.

## Common Greek Expressions

### Greetings
- "Γεια σας" (Hello - formal)
- "Γεια σου" (Hello - informal)
- "Καλημέρα" (Good morning)
- "Καλησπέρα" (Good evening)
- "Χαίρετε" (Greetings - formal)

### Information Requests
- "Θέλω πληροφορίες για..." (I want information about...)
- "Μπορείτε να μου πείτε για..." (Can you tell me about...)
- "Ψάχνω για..." (I'm looking for...)
- "Τι γνωρίζετε για..." (What do you know about...)
- "Χρειάζομαι βοήθεια με..." (I need help with...)

### Polite Expressions
- "Παρακαλώ" (Please)
- "Ευχαριστώ" (Thank you)
- "Συγγνώμη" (Sorry/Excuse me)
- "Αν είναι δυνατόν" (If possible)
- "Θα ήθελα" (I would like)

### Common Question Words
- "Τι" (What)
- "Πού" (Where)
- "Πότε" (When)
- "Πώς" (How)
- "Γιατί" (Why)
- "Ποιος/Ποια/Ποιο" (Who/Which)

## Entity Extraction Examples

### Using Parameters in Training Phrases
```json
{
  "text": "Θέλω πληροφορίες για ",
  "userDefined": false
},
{
  "text": "προϊόντα",
  "alias": "info-type",
  "meta": "@info-type",
  "userDefined": true
}
```

### Common Greek Entities

#### Time Expressions
- "σήμερα" (today)
- "αύριο" (tomorrow)
- "χθες" (yesterday)
- "το πρωί" (in the morning)
- "το απόγευμα" (in the afternoon)

#### Numbers
- "ένα" (one)
- "δύο" (two)
- "τρία" (three)
- "πρώτος" (first)
- "δεύτερος" (second)

#### Locations
- "Αθήνα" (Athens)
- "Θεσσαλονίκη" (Thessaloniki)
- "κέντρο" (center)
- "βόρεια" (north)
- "νότια" (south)

## Grammar Considerations

### Greek Language Specifics
1. **Gender**: Nouns have gender (masculine, feminine, neuter)
2. **Cases**: Greek has four cases (nominative, genitive, accusative, vocative)
3. **Articles**: Definite articles change based on gender and case
4. **Verb Conjugation**: Verbs change based on person, number, tense, and mood

### Training Phrase Variations
Include variations for:
- Different grammatical cases
- Formal vs. informal speech
- Regional dialects
- Common misspellings or alternative spellings

## Examples by Intent Category

### Customer Service
- "Θέλω να κάνω παράπονο" (I want to make a complaint)
- "Έχω πρόβλημα με την παραγγελία μου" (I have a problem with my order)
- "Πώς μπορώ να επιστρέψω ένα προϊόν;" (How can I return a product?)

### Booking/Reservations
- "Θα ήθελα να κλείσω ραντεβού" (I would like to book an appointment)
- "Είναι διαθέσιμη η Τρίτη;" (Is Tuesday available?)
- "Μπορώ να αλλάξω την κράτησή μου;" (Can I change my booking?)

### Product Information
- "Ποια είναι η τιμή του προϊόντος;" (What is the product price?)
- "Έχετε αυτό σε άλλο χρώμα;" (Do you have this in another color?)
- "Πότε θα έρθει σε απόθεμα;" (When will it be back in stock?)

## Best Practices

1. **Use Natural Speech**: Include how people actually speak, not just formal language
2. **Include Variations**: Add synonyms and different ways to express the same intent
3. **Test with Native Speakers**: Validate phrases with Greek native speakers
4. **Regional Differences**: Consider including phrases from different Greek regions
5. **Context Awareness**: Include phrases that make sense in your specific domain

## Common Mistakes to Avoid

1. **Literal Translations**: Don't directly translate from English
2. **Formal Only**: Include both formal and informal speech patterns
3. **Single Word Entities**: Greek often uses different word forms
4. **Ignoring Grammar**: Consider Greek grammatical rules in phrase structure
5. **Limited Vocabulary**: Use diverse vocabulary beyond basic words