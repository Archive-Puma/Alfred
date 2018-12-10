/* eslint-disable  func-names */
/* eslint-disable  no-console */

/*
   ____________________________________________________________________
 / \                                                                   \
|   |                  <>   LENGUAJE: ALFRED   <>                      |
\_ |__         ____                              __           ________|
 |                                                                  |
 |  Skill ID: amzn1.ask.skill.6568da0f-6575-4b54-be12-8b110aaf60f9  |
 |                                                                  |
 |                                                                  |
 |                                                                  |
 |                                                                  |
 |                                                                  |
 |                                                                  |
 |                                                                  |
 |                                                                  |
 |                                                                  |
 |   _______________________________________________________________|__
 |  /                                                                /
 \_/________________________________________________________________/
*/

const Alexa = require('ask-sdk-core');

// -=x=-=x=-=x=-=x=-=x=-=x=-
// !       VARIABLES       ¡
// -=x=-=x=-=x=-=x=-=x=-=x=-

const DIALOGS = {
  'prompt': '¿Qué instrucción deseas que ejecute?',

  'LaunchRequest': {
    'welcome': "Bienvenido al intérprete del lenguaje de programación Alfred. ",
    'onlyrepl': "Actualmente sólo está disponible la versión interactiva, por lo que ejecutaré las instrucciones que me vayas diciendo. ",
    'exit': 'Si deseas salir de la Skill di "Salir" o ejecuta el comando "Adiós Alfred". ',
    'prompt': '¿Qué deseas hacer?'
  }
}

// -=x=-=x=-=x=-=x=-=x=-=x=-
// !        HANDLER        ¡
// -=x=-=x=-=x=-=x=-=x=-=x=-

const LaunchRequestHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'LaunchRequest';
  },
  handle(handlerInput) {

    const reprompt = DIALOGS.LaunchRequest.onlyrepl + DIALOGS.LaunchRequest.exit + DIALOGS.LaunchRequest.prompt;
    const speechText = DIALOGS.LaunchRequest.welcome + reprompt;

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(reprompt)
      .withSimpleCard('Alfred v0.4.0', speechText)
      .getResponse();
  },
};

const ByeCommandHandler = {
  /* Integrado dentro de CancelAndStopIntentHandler */
};


const SayCommandHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest'
      && handlerInput.requestEnvelope.request.intent.name === 'Command_DI';
  },
  handle(handlerInput) {

    const speechText = handlerInput.requestEnvelope.request.intent.slots.texto.value;

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(DIALOGS.prompt)
      .getResponse();
  },
};

const HelpIntentHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest'
      && handlerInput.requestEnvelope.request.intent.name === 'AMAZON.HelpIntent';
  },
  handle(handlerInput) {
    const speechText = 'You can introduce yourself by telling me your name';

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(speechText)
      .getResponse();
  },
};

const CancelAndStopIntentHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest'
      && (handlerInput.requestEnvelope.request.intent.name === 'AMAZON.StopIntent'
        || handlerInput.requestEnvelope.request.intent.name === 'AMAZON.CancelIntent'
        || handlerInput.requestEnvelope.request.intent.name === 'Command_ADIOSALFRED');
  },
  handle(handlerInput) {
    const speechText = '¡Adiós¡';

    return handlerInput.responseBuilder
      .speak(speechText)
      .getResponse();
  },
};

const SessionEndedRequestHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'SessionEndedRequest';
  },
  handle(handlerInput) {
    console.log(`Session ended with reason: ${handlerInput.requestEnvelope.request.reason}`);

    return handlerInput.responseBuilder.getResponse();
  },
};

const ErrorHandler = {
  canHandle() {
    return true;
  },
  handle(handlerInput, error) {
    console.log(`Error handled: ${error.message}`);

    return handlerInput.responseBuilder
      .speak('Sorry, I can\'t understand the command. Please say again.')
      .reprompt('Sorry, I can\'t understand the command. Please say again.')
      .getResponse();
  },
};

const skillBuilder = Alexa.SkillBuilders.custom();

exports.handler = skillBuilder
  .addRequestHandlers(
    LaunchRequestHandler,
    // ByeCommandHandler,
    SayCommandHandler,

    HelpIntentHandler,
    CancelAndStopIntentHandler,
    SessionEndedRequestHandler
  )
  .addErrorHandlers(ErrorHandler)
  .lambda();
