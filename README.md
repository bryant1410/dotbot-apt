# Dotbot APT Plugin

Easily install APT packages wi with [dotbot](https://github.com/anishathalye/dotbot).

Inspired by [dotbot-apt-get](https://github.com/rubenvereecken/dotbot-apt-get).

## Usage

Python 3.5+ is needed.

It's easiest to track this plugin in your dotfiles repo:

```bash
git submodule add https://github.com/bryant1410/dotbot-apt
```

I also recommend having your apt-get list in a separate file since dotbot will need root privileges to use the plugin.
Using the plugin will look something like this:

```bash
./install -p dotbot-apt/apt.py -c packages.conf.yaml
```
