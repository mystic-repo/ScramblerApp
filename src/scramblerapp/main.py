#!/usr/bin/python3 -B
from tkinter.filedialog import Open
from .scrambler import Scrambler, ScramblerGUI
from .gui.encryptiongui import EncryptionGUI
from .gui.stashgui import StashGUI
from .dircrawler.instance import Instance
from .utils.configparser import ConfigParser

from .utils.encryption import OpenSSLEncyptor

def main():
	scrambler = Scrambler()
	instance = Instance()
	configparser = ConfigParser()
	encryptiongui = EncryptionGUI(scrambler, instance)
	stashgui = StashGUI(scrambler, instance, configparser)
	scramblergui = ScramblerGUI(scrambler, instance, encryptiongui, stashgui)
	scramblergui.run()

if __name__ == '__main__':
	raise SystemExit(main())