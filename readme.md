# pilotfish

I needed to figure out how to attach a child window to the side of
a PySimpleGUI-based program's main window.  In the process of working
that out, I got side-tracked by this little time-waster.

Grab and move the shark, and the pilotfish follows (or leads --
depending on which of three possible relative positions is randomly
selected at run time.)  

Right-click on the shark and choose **Exit** to close the program.

![Screenshot](https://github.com/therden/pilotfish/raw/master/images/Screenshot_Linux.png "Pilotfish and blue shark")

The above screenshot is from Windows OS, in which only the fishes will be visible (the windows that containing their images are transparent.) Neither Linux nor, I believe, Mac OS supports that TCL feature, so they'll display each fish in its own rectangular blue window. (So wait... Windows is *cooler*?!?)

Right-click on the shark and choose **Add another pair** to propagate another
shark and her pilotfish pal.

![Screenshot](https://github.com/therden/pilotfish/raw/master/images/Screenshot_Windows.jpg "Blue sharks and pilotfishes")

I'm probably done fooling with this, but

### Maybe/Someday...
* Auto-pilot mode -- shark and pilotfish move without intervention
* Pilotfish occasionally changes its position relative to shark within session
