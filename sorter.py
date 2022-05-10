from pathlib import Path
from shutil import move
import json

CUR_DIR = Path.cwd()
HOME = Path.home()
DOWNLOADS = HOME / "Downloads"
MYDOCS = HOME / "Documents"
DESKTOP = HOME / "Desktop"

shortcuts = [DOWNLOADS,MYDOCS,DESKTOP]

class Sorter():
    def __init__(self,dir) -> None:
        self.dir = Path(dir)

    def check_dir(self):
        if not self.dir.is_dir():
            return False
        return True

    def get_manifestExt(self):
        with open("sorted_files.json","r",encoding="utf-8") as f:
            return json.load(f)
        
    def get_files(self):
        return [f for f in self.dir.glob("*")]
    
    def add_to_resolve(self,ext):
        with open("resolve_list.json","r") as f:
            entries = json.load(f)
        if ext not in entries:
            entries.append(ext)
            with open("resolve_list.json","w") as f:
                json.dump(entries,f,indent=4)
        
    def sort(self):

        files = self.get_files()
        manifest = self.get_manifestExt()

        for f in files:
            found = False
            for ftype in manifest:
                if found == True:
                    break

                if (f.suffix).lower() in manifest[ftype]:
                    Path.mkdir(self.dir / ftype, exist_ok=True)
                    if Path(self.dir / ftype / f.name).is_file():
                        f.rename(Path(f"{self.dir / ftype / f.name}_duplicate"))
                    else:
                        f.rename(self.dir / ftype / f.name)
                    found = True

                elif f.is_dir() and f.name not in manifest.keys():
                    Path.mkdir(self.dir / "Dossier", exist_ok=True)
                    move(src=(self.dir / f),dst=(self.dir / "Dossier"))
                    found = True

                elif f.name in manifest.keys():
                    found = True
                    break
                
            if found == False:
                Path.mkdir(self.dir / "Autre", exist_ok=True)
                self.add_to_resolve(ext=f.suffix)
                f.rename(self.dir / "Autre" / f.name)
                
if __name__ == "__main__":
    # sorter = Sorter(r"C:\Users\RMansouri\Downloads")
    # sorter.sort()
    pass
