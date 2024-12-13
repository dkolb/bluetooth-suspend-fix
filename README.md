# ESpeak as Say

This is a hyper niche RPM package that essentially installs a recommended
workaround for a suspend issue involving bluetooth in the 6.11.X kernel.

This is an RPM package because I use an ostree based fedora distribution.

# Installing from Copr

# Building the Package Locally

1. Drop into a distrobox for fedora if necessary
2. `dnf install tito`
3. `tito build --rpm --test`
4. Note the path output in the terminal similar to this: `/tmp/tito/x86_64/espeak-as-say-1.0.3-2.git.0.d603485.fc40.x86_64.rpm`
5. Return to your normal terminal
6. `rpm-ostree install ${PATH_FROM_STEP_4}`
7. Reboot into new ostree
8. Enjoy TTS from IINACT + Cactbot I guess.
