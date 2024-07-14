# Local Inference Voice Assitant on a Dell R630 Server with LLaMA3 and Whisper

## Project Overview

This project aims to create a CPU-only local inference system using a Dell PowerEdge R630 server. The goal is to integrate LLaMA for text generation and Whisper for speech recognition to enable interactive voice-based question-and-answer sessions.

## Background

I received a Dell PowerEdge R630 server from a friend and decided to leverage its robust CPU resources for this project. Given the server lacks GPUs, the focus will be on optimizing inference to run efficiently on CPUs. I chose Ubuntu Server for its stability and extensive support for machine learning libraries.

## Hardware

- **Server:** Dell PowerEdge R630
  - **CPU:** Dual Intel Xeon E5-2600 v3/v4 processors
  - **Memory:** 96 GB
  - **Storage:** 600 GB
- **Microphone and Speakers:** For voice input and output

## Software

- **Operating System:** Ubuntu Server
- **Machine Learning Libraries:**
  - IPEX-LLM (Intel Extension for PyTorch)
  - Transformers (for LLaMA)
  - [Whisper.cpp](https://github.com/ggerganov/whisper.cpp) (for STT)
- **Python Libraries:**
  - PyAudio (for audio input/output)
  - gTTS (for text-to-speech)
 
## Road blocks

- Need to buy a longer patch cable so I can use iDRAC over the network.
- Need to solve a mismatched PSU issue (suspect firmware)
- Booting from USB failed, the server did not recognize the bootable media

## Project Plan

### 1. Install the Operating System

- Download and install Ubuntu Server on the Dell PowerEdge R630.
- Ensure all system updates are applied.

### 2. Prepare the Environment

- Decide whether to develop locally, on the server using vim, or remotely on the server though setting up iDRAC.

### 3. Install Required Libraries

- Install IPEX-LLM, Transformers, Whisper.cpp, and PyAudio into a python enviroment.

### 4. Write scripts

- Develop scripts for recording audio, transcribing speech, generating responses, and playing audio.

## Conclusion

This project plan outlines the steps to create a CPU-only local inference system on the Dell PowerEdge R630 server. The integration of LLaMA and Whisper will enable a full audio-based interaction system, leveraging the server's robust CPU resources efficiently.
