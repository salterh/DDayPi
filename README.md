# DDayPi

## TODO 

- [ ] Bash script to setup Pi's with sound library & PD etc @spearse
- [ ] Setup OSC Message glossary/terms
- [ ] Settle on OSC networking structure
- [ ] Bash script for setting up WIFI broadcasting @spearse
- [ ] Basic sound playback 
- [ ] Sound playback with or without fading
- [ ] Compostional structure & layering
- [ ] \(optional) Settle on DSP tools/effects?
- [ ] Startup script - needs to differentiate between main & subsidiary /server client


### OSC Message Structure

/Address | Team Number/Name | Information

### OSC Message Glossary
#### Addresses
##### Top Level Addresses

- /All (For information every Pi needs to know)
- /Main (For information the main Pi needs to know)
- /Subs (For information every Pi *but* the main Pi needs to know)

##### Lower Level Addresses

- /Answer (For information regarding the guessing of answers)
- /Help (Alerts the system that a certain team needs a member of staff)
- /Hint (Gives the team a hint)

#### Team Number/Name

#### Information

