const assert        = require('assert');
const expect        = require('chai').expect;
const VirtualAlexa  = require("virtual-alexa").VirtualAlexa;

const lambda = "us-east-1_ask-custom-alexa-default";

const DIALOGS = {
  'speak':  [ '<speak>', '</speak>' ],
  'prompt': '¿Qué instrucción deseas que ejecute?',

  'LaunchRequest': "Bienvenido al intérprete por voz del lenguaje de programación Alfred. Ejecutaré las instrucciones que me vayas diciendo de una en una. Si necesitas ayuda prueba a decir \"Ayuda\". Si deseas salir de la Skill di \"Salir\" o ejecuta el comando \"Adiós Alfred\". ¿Qué deseas hacer?"
};

speak = (dialog) => DIALOGS.speak[0] + dialog + DIALOGS.speak[1];

describe('[Unit Test] Lenguaje: Alfred', function() {

  let alexa = VirtualAlexa.Builder()
    .handler("../" + lambda + "/index.handler")
    .interactionModelFile("../../models/es-ES.json")
    .create();

  it('Launch Request', async function() {
    const res = await alexa.launch();
    expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.LaunchRequest));
  });
});

// https://github.com/blutag-dev/alexa-unit-test-simple-mock
