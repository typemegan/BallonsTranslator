from gallery_dl.job import DownloadJob
from gallery_dl import config
from qtpy.QtCore import QObject, Signal, QThread
from utils.logger import logger as LOGGER
from ui.misc import ProgramConfig
from ui.imgtrans_proj import ProjImgTrans

class SourceDownload(QThread):
    open_downloaded_proj = Signal(str)
    update_progress_bar = Signal(int)
    finished_downloading = Signal()

    def __init__(self, config: ProgramConfig, imgtrans_proj: ProjImgTrans, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = None
        self.config_pnl = config
        self.imgtrans_proj = imgtrans_proj
        self.path = ''
        self.url = ''

    def ReturnFullPathToProject(self) -> str:
        return self.path

    def ValidateUrl(self):
        if 'https://' not in self.url:
            self.url = 'https://' + self.url

    def PassUrlToImgTransProj(self):
        self.imgtrans_proj.src_download_link = self.url

    def FetchImages(self):
        config.load()
        job = DownloadJob(self.url)
        job.run()
        self.path = job.pathfmt.directory

    def openDownloadedProj(self, proj_path):
        self.open_downloaded_proj.emit(proj_path)

    def _SyncSourceDownload(self):
        #  TODO keep track of downloaded page
        #  TODO edit DownloadJob to always include url
        import time
        for i in range(100):
            self.update_progress_bar.emit(i)
            LOGGER.info(i)
            time.sleep(0.05)
        self.url = self.config_pnl.src_link_flag
        if self.url:
            LOGGER.info(f'Url set to {self.url}')

            self.ValidateUrl()
            self.FetchImages()
            self.PassUrlToImgTransProj()

            proj_path = self.ReturnFullPathToProject()
            LOGGER.info(f'Project path set to {proj_path}')

            if proj_path:
                self.openDownloadedProj(proj_path)

            self.finished_downloading.emit()

    def run(self):
        self._SyncSourceDownload()