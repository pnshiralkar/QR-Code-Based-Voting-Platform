# QR-code-based-voting-platform

This platform was developed for voting photos/sketches using QR Codes in exhibition - Picsoreel (by college student group [Pictoreal](http://www.pictoreal.in)). Also, the platform used barcode based ID Cards of students to confirm identity.

# Modules : 
### Authentication : 
* Volunteers register the audience from admin login (/adminlogin) using barcode scanner.
* Once registered, audience are able to login from home page(/) by again scanning their ID Card barcode.
* This is done to ensure that no one votes twice

### Voting :
* Once logged in, audience need to scan the QR Code of the photo/sketch they want to vote. (/vote)
* Once finished voting, they submit the votes.

### Results :
* The results are calculated at runtime at route /count (accessible only to the admin and volunteers).

# Technology used:

#### &nbsp;&nbsp;&nbsp;&nbsp; Backend : Django, PostgreSQL
#### &nbsp;&nbsp;&nbsp;&nbsp; Frontend : HTML, CSS, Javascript, jQuery, Materialize-css
#### &nbsp;&nbsp;&nbsp;&nbsp; QR Code scanner JS Library : InstaScan
#### &nbsp;&nbsp;&nbsp;&nbsp; Barcode scanner JS Library : QuaggaJS
#### &nbsp;&nbsp;&nbsp;&nbsp; Deployment : Docker, Azure VM
