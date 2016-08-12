
import os
from pocketsphinx import pocketsphinx
from sphinxbase import sphinxbase
import pyaudio
import requests
import json


def start_keyphrase_recognition(keyphrase_function, key_phrase):
    """ Starts a thread that is always listening for a specific key phrase. Once the
        key phrase is recognized, the thread will call the keyphrase_function. This
        function is called within the thread (a new thread is not started), so the
        key phrase detection is paused until the function returns.

    :param keyphrase_function: function that is called when the phrase is recognized
    :param key_phrase: a string for the key phrase
    """
    modeldir = "files/sphinx/models"

    # Create a decoder with certain model
    config = pocketsphinx.Decoder.default_config()
    config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
    config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
    config.set_string('-keyphrase', key_phrase)
    config.set_string('-logfn', 'files/sphinx.log')
    config.set_float('-kws_threshold', 5)

    # Start a pyaudio instance
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print numdevices
    print "\n"

    # for each audio device, determine if is an input or an output and
    # add it to the appropriate list and dictionary
    for i in range(0, numdevices):
        if p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0:
            print "Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name')

        if p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels') > 0:
                print "Output Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name')

    devinfo = p.get_device_info_by_index(1)
    print "Selected device is ", devinfo.get('name')
    if p.is_format_supported(44100,  # Sample rate
                             input_device=devinfo["index"],
                             input_channels=devinfo['maxInputChannels'],
                             input_format=pyaudio.paInt16):
                    print 'Yay !'

    # Create an input stream with pyaudio
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
    # Start the stream
    stream.start_stream()

    # Process audio chunk by chunk. On keyword detected perform action and restart search
    decoder = pocketsphinx.Decoder(config)
    decoder.start_utt()

    # Loop forever
    while True:
        # Read 1024 samples from the buffer
        buf = stream.read(4096)
        # If data in the buffer, process using the sphinx decoder
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
        # If the hypothesis is not none, the key phrase was recognized
        if decoder.hyp() is not None:
            keyphrase_function()
            # Stop and reinitialize the decoder
            decoder.end_utt()
            decoder.start_utt()


url = 'https://swear-jar-office.herokuapp.com/swear/jar/'
# url = 'http://127.0.0.1:8000/swear/jar/'
payload = {
    'name': 'Davide'
}


def swear_function():
    requests.put(url, data=json.dumps(payload))
    print("You sweared!!!")


if __name__ == "__main__":
    # Start key phrase recognition and call the "demo_function" when triggered
    start_keyphrase_recognition(swear_function, "shit")
