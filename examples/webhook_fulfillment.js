// Example webhook fulfillment for Greek Dialogflow agent
// This is a basic Node.js example using Express.js

const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Webhook endpoint
app.post('/webhook', (req, res) => {
  const intentName = req.body.queryResult.intent.displayName;
  const parameters = req.body.queryResult.parameters;
  
  let responseText = '';
  
  switch (intentName) {
    case 'Get Information':
      const infoType = parameters['info-type'];
      responseText = handleInformationRequest(infoType);
      break;
      
    case 'Default Welcome Intent':
      responseText = 'Καλώς ήρθατε! Πώς μπορώ να σας βοηθήσω;';
      break;
      
    case 'Goodbye':
      responseText = 'Αντίο! Ελπίζω να σας βοήθησα!';
      break;
      
    default:
      responseText = 'Συγγνώμη, δεν μπόρεσα να καταλάβω την αίτησή σας.';
  }
  
  const response = {
    fulfillmentText: responseText,
    fulfillmentMessages: [
      {
        text: {
          text: [responseText]
        }
      }
    ]
  };
  
  res.json(response);
});

function handleInformationRequest(infoType) {
  const responses = {
    'προϊόντα': 'Διαθέτουμε μεγάλη ποικιλία προϊόντων υψηλής ποιότητας.',
    'υπηρεσίες': 'Προσφέρουμε εξειδικευμένες υπηρεσίες για όλες τις ανάγκες σας.',
    'τιμές': 'Οι τιμές μας είναι ανταγωνιστικές. Επικοινωνήστε μαζί μας για προσφορά.',
    'διαθεσιμότητα': 'Μπορείτε να ελέγξετε τη διαθεσιμότητα στο κατάστημά μας.',
    'ωράριο': 'Λειτουργούμε Δευτέρα-Παρασκευή 9:00-17:00.',
    'επικοινωνία': 'Μπορείτε να μας βρείτε στο τηλέφωνο 210-1234567 ή στο email info@example.gr'
  };
  
  return responses[infoType] || 'Δυστυχώς δεν έχω πληροφορίες για αυτό που ζητάτε.';
}

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Webhook server running on port ${PORT}`);
});

module.exports = app;