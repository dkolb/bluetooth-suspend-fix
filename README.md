# ESpeak as Say

[![Copr build status](https://copr.fedorainfracloud.org/coprs/dkubs/espeak-as-say/package/espeak-as-say/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/dkubs/espeak-as-say/package/espeak-as-say/)

This is a hyper niche RPM package that essentially installs a bash script to `/usr/bin/say`
allowing programs that expect the old `say` to instead call espeak.

This is an RPM package because I use Bazzite and it seemed really weird and
annoying to setup a whole blue build image and constantly publish new images
all for what could just be a layered RPM package.

# Installing from Copr

1. Depending on if your system supports the `dnf copr` command:
    a. `dnf copr enable dkubs/espeak-as-say`
    b. `sudo curl -o /etc/yum.repos.d/_copr_dkubs-espeak-as-say.repo 'https://copr.fedorainfracloud.org/coprs/dkubs/espeak-as-say/repo/fedora-40/dkubs-espeak-as-say-fedora-40.repo'`
2. `rpm-ostree install espeak-as-say`

# Building the Package Locally

1. Drop into a distrobox for fedora if necessary
2. `dnf install tito`
3. `tito build --rpm --test`
4. Note the path output in the terminal similar to this: `/tmp/tito/x86_64/espeak-as-say-1.0.3-2.git.0.d603485.fc40.x86_64.rpm`
5. Return to your normal terminal
6. `rpm-ostree install ${PATH_FROM_STEP_4}`
7. Reboot into new ostree
8. Enjoy TTS from IINACT + Cactbot I guess.
