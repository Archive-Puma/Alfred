const assert        = require('assert');
const expect        = require('chai').expect;
const VirtualAlexa  = require("virtual-alexa").VirtualAlexa;

const lambda = "us-east-1_ask-custom-alexa-default";

const DIALOGS = {
  'speak':  [ '<speak>', '</speak>' ],
  'prompt': '¿Qué instrucción deseas que ejecute?',

  'LaunchRequest':  "Bienvenido al intérprete por voz del lenguaje de programación Alfred. Ejecutaré las instrucciones que me vayas diciendo de una en una. Si necesitas ayuda prueba a decir \"Ayuda\". Si deseas salir de la Skill di \"Salir\" o ejecuta el comando \"Adiós Alfred\". ¿Qué deseas hacer?",
  'HelpRequest':    "Las instrucciones disponibles actualmente son: Di, Define la variable, Muestra el tipo de, Muestra el valor de, Adiós Alfred. ¿Qué instrucción deseas que ejecute?",
  'StopRequest':    "Cerrando la Skill... ¡Adiós!"
};

speak = (dialog) => DIALOGS.speak[0] + dialog + DIALOGS.speak[1];

describe('[Unit Test] Lenguaje: Alfred (es-ES)', function() {

  let alexa = VirtualAlexa.Builder()
    .handler("../" + lambda + "/index.handler")
    .interactionModelFile("../../models/es-ES.json")
    .create();

  it('Launch Request', async function() {
    const res = await alexa.launch();
    expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.LaunchRequest));
  });

  it('Help Request', async function() {
    let res;
    res = await alexa.utter("ayuda");
    expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.HelpRequest));
    res = await alexa.utter("comandos");
    expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.HelpRequest));
    res = await alexa.utter("necesito ayuda");
    expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.HelpRequest));
  });

  it('Stop Request', async function() {
    let res;
    res = await alexa.utter("salir");
    expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.StopRequest));
    res = await alexa.utter("salir de la skill");
    expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.StopRequest));
  });
  
  it('"Command: Say" Request', async function() {
    let res;
    res = await alexa.utter("di");
    expect(res.response.outputSpeech.ssml).to.equal(speak(""));
    res = await alexa.utter("di di");
    expect(res.response.outputSpeech.ssml).to.equal(speak("di"));
    res = await alexa.utter("di joder");
    expect(res.response.outputSpeech.ssml).to.equal(speak("joder"));
    res = await alexa.utter("di hola mundo");
    expect(res.response.outputSpeech.ssml).to.equal(speak("hola mundo"));
  });

  it('"Command: ByeAlfred" Request', async function() {
    let res;
    // FIXME: "Adios" Utterance Error
    // res = await alexa.utter("adios");
    // expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.StopRequest));
    // FIXME: "Adios Alfred" Utterance Error
    // res = await alexa.utter("adiós alfred");
    // expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.StopRequest));
    res = await alexa.utter("adiós alfred");
    expect(res.response.outputSpeech.ssml).to.equal(speak(DIALOGS.StopRequest));
  });
});

// https://github.com/blutag-dev/alexa-unit-test-simple-mock
