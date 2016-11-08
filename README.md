# md5-for-droplet
A command line tool to obtain the md5 hash of an rsa ssh public key 'id_rsa.pub' produced by ssh-keygen. For use with Digital Ocean's `doctl computer droplet create` command.

## Installation
`git clone https://github.com/aaronfowles/md5-for-droplet`

## Usage
The following will write the md5 component of the key at `$HOME/.ssh/id_dsa.pub` to standard out.

`cd md5-for-droplet`

`python __main__.py --file $HOME/.ssh/id_dsa.pub`
