# DDayPi

## Spec 

An interactive timeloop soundscape which presents aural opportunities for participants to find clues and answer questions in interesting ways. Participants should listen closely to audio clues and pay attention to their surroundings to answer questions which meaningfully change the soundscape.

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

#### Examples

/All/Answer/1/"France"
/Self/Hint/1/"bang"
/Subs/Help/2/""

