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

## Project Plan

### 1. Prepared the Environment

- Bought a long enough cat6 patch cable to get from my router to the iDRAC port of the server.
- Accessed iDRAC for the server on my home network - there were conflicts between a previous static ip and using DHCP so I set the static IP to one on my network
- Accessed virtual console
    - downloaded .jnlp file onto my laptop from iDRAC
    - downgraded my JDK to 11 because modern Java versions deprecated the Java Web Start technology used by iDRAC.
    - downloaded IcedTea-Web which includes the javaws command for opening jnlp files
    - Set up Java Web Start with settings detailed in a private file
  
### 2. Install the Operating System

- Booting from USB failed, the server did not recognize the bootable media
- Used iDRAC to Download and install Ubuntu Server on the Dell PowerEdge R630.
- Formatted the hard drive with 176 GB swap space in an LVM volume to handle the planned memory intensive tasks

### 3. Install Required Libraries

- Got permission to access Llama3 repos
-  huggingface-cli login
- entered token
- Install IPEX-LLM, Transformers, Whisper.cpp, and PyAudio into a python enviroment.

### 4. Write scripts

- Develop scripts for recording audio, transcribing speech, generating responses, and playing audio.


## Misc.

- Need to solve a mismatched PSU issue (suspect firmware)

## Conclusion

This project plan outlines the steps to create a CPU-only local inference system on the Dell PowerEdge R630 server. The integration of LLaMA and Whisper will enable a full audio-based interaction system, leveraging the server's robust CPU resources efficiently.
