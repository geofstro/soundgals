soundgals
=========

Computer Audio Development

This is an update to the XBMC/Kodi plug in; Qobuz XBMC.

The update adds a new "Audiophile" option under the add-on settings within the XBMC/Kodi GUI.

When this option is selected via its radio button, each time a user selects either an album or playlist from within
Qobuz XBMC a file named qobuzNow.m3u8 will be written as a playlist which contains all the urls necessary to
play the files from this playlist. If the file qobuzNow.m3u8 doesn't exist it will be created. The file is written
to the users Music directory within his/her home directory of the OS.

The user must have designated a program to open all files of type .m3u8 within his/her operating system.

This should be a program such as foobar2000, HQPlayerDesktop, J River Media center or VLC, since all of these support
flac streaming.

As long as a default program which supports flac streaming is chosen in the os by the user, the qobuzNow.m3u8 file
will be opened by that program.

Turning the "Audiophile" feature off will cause Qobuz XBMC to revert to its default behaviour of playing Qobuz
streams through XBMC.

Version 1.1.1 Now adds the support for individual tracks to take advantage of this "Audiophile" option.
For this to work you must turn off "Play the next song automatically" under Sytem -> Settings -> Music -> Playback.


