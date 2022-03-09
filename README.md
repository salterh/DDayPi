# DDayPi

## Spec 

An interactive timeloop soundscape which presents aural opportunities for participants to find clues and answer questions in interesting ways. Participants should listen closely to audio clues to answer questions which change the soundscape. The soundscape will evolve to fit into the narrative of the ship itself; DDay -> Nightclub -> Salvage -> Sinking (repeat infinitely, or until the timeloop is broken). 

## TODO 

- [ ] Bash script to setup Pi's with sound library & PD etc @spearse
- [ ] Setup OSC Message glossary/terms
- [ ] Settle on OSC networking structure
- [ ] Setup OSC in PD
- [ ] Bash script for setting up WIFI broadcasting @spearse
- [ ] Basic sound playback 
- [ ] Sound playback with or without fading
- [ ] Compostional structure & layering
- [ ] \(optional) Settle on DSP tools/effects?
- [ ] Startup script - needs to differentiate between main & subsidiary /server client


### OSC Message Structure

/High Level Address /Low Level Address | Team Number/Name | Information

### OSC Message Glossary
#### Addresses
##### Top Level Addresses
*Note; not all of these may be necessary.*

- /All (For information every Pi needs to know).
- /Main (For information the main Pi needs to know).
- /Subs (For information every Pi *but* the main Pi needs to know).
- /# (For information only one Pi needs to know).
- /Self (For information only this Pi needs to know).

##### Lower Level Addresses

- /Answer (For information regarding the guessing of answers).
- /Help (Alerts the system that a certain team needs a member of staff).
- /Hint (Gives the team a hint).

#### Team Number/Name

This depends on the amount of teams present at once, and whether or not the naming of teams is allows.

#### Information
*This is the information given by the participants. Below is a list of possible inputs to consider.*

- Morse Code (physical machine/lights/sound).
- Typewriter
- Buttons
- reacTIVision
- LEAP Motion


