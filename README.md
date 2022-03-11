# DDayPi

## Spec 

An interactive timeloop soundscape which presents aural opportunities for participants to find clues and answer questions in interesting ways. Participants should listen closely to audio clues to answer questions which change the soundscape. The soundscape will evolve to fit into the narrative of the ship itself; DDay -> Nightclub (repeat infinitely, or until the timeloop is broken). 

## TODO 

- [ ] Bash script to setup Pi's with sound library & PD etc @spearse
- [x] Setup OSC Message glossary/terms
- [x] Settle on OSC networking structure
- [x] Setup OSC in PD
- [ ] Bash script for setting up WIFI broadcasting @spearse
- [x] Basic sound playback 
- [ ] Sound playback with or without fading
- [ ] Compostional structure & layering
- [ ] \(optional) Settle on DSP tools/effects?
- [ ] Startup script - needs to differentiate between main & subsidiary /server client


### OSC Message Structure

/Address/Team Number/Information

### OSC Message Glossary
#### Addresses
*Note; not all of these may be necessary.*

- /All (For information all Pi's need to know)
- /Subs (For information sub Pi's need to know)
- /Self (For information this Pi needs to know)

- /Answer (The inputting of answers).
- /Help (Alerts the system that a certain team needs a member of staff).
- /Hint (Gives the team a hint).

#### Information
*This is the information given by the participants. Below is a list of possible inputs to consider.*

- Morse Code (physical machine/lights/sound).
- Typewriter
- Buttons
- reacTIVision
- LEAP Motion


