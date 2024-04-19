from win32com.shell import shell, shellcon
from pathlib import Path
class KillBar:
    def __init__(self, ch) -> None:
        self.ch = ch
        self.cleanNeed = False
        path = shell.SHGetKnownFolderPath(shellcon.FOLDERID_Videos)
        self.folder = Path(f"{path}\Hunt  Showdown")#\Hunt  Showdown
        if not self.folder.is_dir():
            self.checked = False
        else:
            self.checked = True
            listfiles = list(self.folder.iterdir())
            self.countKill = len(listfiles)
            print(self.countKill)

    def update(self):
        if(self.cleanNeed):
            self.ch.drawKill("clear")
            self.cleanNeed = False
        if(self.countKill != len(list(self.folder.iterdir()))):
            self.countKill = len(list(self.folder.iterdir()))
            self.ch.drawKill("kill")
            self.cleanNeed = True