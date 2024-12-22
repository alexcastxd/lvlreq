# gd_lvlreq (for Streamlabs Chatbot)
Script for Streamlabs Chatbot that lets you do level requests without any other tools

regex tester (just in case idk): https://regexr.com/

## Requirements:

- Streamlabs Chatbot (ofc xd)
  - Requires Python 2.7.13
- gd.py (API for GD in Python)
  - Requires Python 3.8+


## Limitations:

The first regex found is the only one to trigger, per message.

If a message has 2 regex patterns, it will stop responding after the first one (based entirely on where the regex is on the regex list file). If you want one phrase to trigger rather than another one, place it higher on the list.

## HUGE THANKS
- syrsly for his [**regex script**](https://github.com/syrsly/StreamlabsChatbotSmartRegex) for the Chatbot
- everyone involved in [**gd.py**](https://github.com/nekitdev/gd.py)'s development (just made everything 100 times easier xd)
