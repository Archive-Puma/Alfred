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

const VARIABLES = {};
const AVAILABLE_COMMANDS = [
  "Di", "Define la variable", "Muestra el tipo de", "Muestra el valor de", "Adiós Alfred" ];

const DIALOGS = {
  'prompt': '¿Qué instrucción deseas que ejecute?',

  'LaunchRequest': {
    'welcome':  "Bienvenido al intérprete por voz del lenguaje de programación Alfred. ",
    'onlyrepl': "Ejecutaré las instrucciones que me vayas diciendo de una en una. ",
    'help':     'Si necesitas ayuda prueba a decir "Ayuda". ',
    'exit':     'Si deseas salir de la Skill di "Salir" o ejecuta el comando "Adiós Alfred". ',
    'prompt':   "¿Qué deseas hacer?"
  },
  'HelpRequest': {
    'instructions': "Las instrucciones disponibles actualmente son: " + AVAILABLE_COMMANDS.join(", ") + ". "
  },
  'ExitRequest': {
    'exit':     "Cerrando la Skill... ¡Adiós!"
  },
  'Unhandled': {
    'error':    "Perdona, no he entendido lo que me has dicho. "
  }
};

// -=x=-=x=-=x=-=x=-=x=-=x=-
// !        HANDLER        ¡
// -=x=-=x=-=x=-=x=-=x=-=x=-

const LaunchRequestHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'LaunchRequest';
  },
  handle(handlerInput) {

    const reprompt   = DIALOGS.LaunchRequest.onlyrepl + DIALOGS.LaunchRequest.help + DIALOGS.LaunchRequest.exit + DIALOGS.LaunchRequest.prompt;
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

const SlotConfirmationHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest' &&
           request.dialogState !== 'COMPLETED' &&
           request.intent.name === 'Command_DEFINE';
  },
  handle(handlerInput) {
    const currentIntent = handlerInput.requestEnvelope.request.intent;
    return handlerInput.responseBuilder
      .addDelegateDirective(currentIntent)
      .getResponse();
  },
};

const DefineCommandHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest'
      && handlerInput.requestEnvelope.request.intent.name === 'Command_DEFINE';
  },
  handle(handlerInput) {

    let speechText;

    const name    = handlerInput.requestEnvelope.request.intent.slots.nombre.value;
    const value   = handlerInput.requestEnvelope.request.intent.slots.valor.value;

    if(name === undefined)
      speechText = 'No he entendido el nombre de la variable. Por favor, di DEFINE LA VARIABLE junto con el nombre que desees ponerle.';
    else {

      const action = (VARIABLES[name] === undefined) ? "definida" : "modificada";

      VARIABLES[name] = value;

      speechText = "La variable " + name + " igual a " + value + " ha sido correctamente " + action + ".";
    }

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(DIALOGS.prompt)
      .getResponse();
  },
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

const ShowTypeCommandHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest'
      && handlerInput.requestEnvelope.request.intent.name === 'Command_MUESTRATIPO';
  },
  handle(handlerInput) {

    let speechText;

    const name = handlerInput.requestEnvelope.request.intent.slots.nombre.value;

    if(name === undefined)
      speechText = 'No he entendido el nombre de la variable. Por favor, di MUESTRA EL TIPO DE junto con el nombre que desees ponerle.';
    else {

      if(VARIABLES[name] === undefined)
        speechText = "No existe ninguna variable " + name + " que haya sido definida.";
      else {

        let type = typeof(VARIABLES[name]);
        if(type === "string")       type = "texto";
        else if(type === "number")  type = "número";

        speechText = "La variable " + name + " contiene un " + type + ".";
      }
    }

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(DIALOGS.prompt)
      .getResponse();
  },
};

const ShowValueCommandHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest'
      && handlerInput.requestEnvelope.request.intent.name === 'Command_MUESTRAVALOR';
  },
  handle(handlerInput) {

    let speechText;

    const name = handlerInput.requestEnvelope.request.intent.slots.nombre.value;

    if(name === undefined)
      speechText = 'No he entendido el nombre de la variable. Por favor, di MUESTRA EL VALOR DE junto con el nombre que desees ponerle.';
    else {

      if(VARIABLES[name] === undefined)
        speechText = "No existe ninguna variable " + name + " que haya sido definida.";
      else
        speechText = "" + VARIABLES[name];
    }

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

    const speechText = DIALOGS.HelpRequest.instructions + DIALOGS.prompt;
    const reprompt   = DIALOGS.LaunchRequest.onlyrepl + DIALOGS.LaunchRequest.help + DIALOGS.LaunchRequest.exit + DIALOGS.LaunchRequest.prompt;


    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(reprompt)
      .getResponse();
  },
};

const UnhandledHandler = {
  canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest'
      && handlerInput.requestEnvelope.request.intent.name === 'Unhandled';
  },
  handle(handlerInput) {

    const speechText = DIALOGS.Unhandled.error + DIALOGS.LaunchRequest.help + DIALOGS.LaunchRequest.exit + DIALOGS.LaunchRequest.prompt;
    const reprompt   = DIALOGS.LaunchRequest.onlyrepl + DIALOGS.LaunchRequest.help + DIALOGS.LaunchRequest.exit + DIALOGS.LaunchRequest.prompt;

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(reprompt)
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
    return handlerInput.responseBuilder
      .speak(DIALOGS.ExitRequest.exit)
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

    console.log("[ERROR] " + error.message);

    const speechText = DIALOGS.Unhandled.error + DIALOGS.LaunchRequest.help + DIALOGS.LaunchRequest.exit + DIALOGS.LaunchRequest.prompt;
    const reprompt   = DIALOGS.LaunchRequest.onlyrepl + DIALOGS.LaunchRequest.help + DIALOGS.LaunchRequest.exit + DIALOGS.LaunchRequest.prompt;

    return handlerInput.responseBuilder
      .speak(speechText)
      .reprompt(reprompt)
      .getResponse();
  },
};

const skillBuilder = Alexa.SkillBuilders.custom();

exports.handler = skillBuilder
  .addRequestHandlers(
    LaunchRequestHandler,
    SlotConfirmationHandler,
    // ByeCommandHandler,
    DefineCommandHandler,
    SayCommandHandler,
    ShowTypeCommandHandler,
    ShowValueCommandHandler,

    UnhandledHandler,
    HelpIntentHandler,
    CancelAndStopIntentHandler,
    SessionEndedRequestHandler
  )
  .addErrorHandlers(ErrorHandler)
  .lambda();
