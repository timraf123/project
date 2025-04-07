# This would require the current user to enter their password again before proceeding.
import system
import clr
currentUser = system.security.getUsername()
password = system.gui.passwordBox("Confirm Password")
valid = system.security.validateUser(currentUser, password)
if valid:
  print ("Logged on")
  system.gui.errorBox("Incorrect password")