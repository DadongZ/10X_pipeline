import subprocess
import yaml

class YmlSettings():
    """Load setting.yml file.
    """
    PIPELINE_VERSION = '1.0.0'

    def __init__(self, setting_file):
        """
        Arg:
            setting_file (str): name of the yaml file for global settings  
        """
        with open(setting_file, 'r') as stream:
            try:
                yml = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                print(err)
        self.makefastq = yml['makefastq']
        self.getcounts = yml['getcounts']
        self.showcmd   = yml['showcmd']
        self.singularity = yml['singularity']
        self.cranger_image  = yml['cranger_image']
        self.projid   = yml['projid']
        self.datadir  = yml['datadir']
        self.refdir   = yml['refdir']
        self.outdir   = yml['outdir']
        self.logdir   = yml['logdir']
        self.cjobs  = yml['cjobs']
        self.ccores = yml['ccores']
        self.fcores = yml['fcores']
        self.ncells = yml['ncells']
        self.sampleids = yml['sampleids']
        self.samplesheet = yml['samplesheet']
        self.sampleskip  = yml['sampleskip']
        self.sampleidcol = yml['sampleidcol']
        self.sampledelim = yml['sampledelim']

    def print_pg(self):
        """Print programs and version to be used
        """
        print(f'The current pipeline version is {YmlSettings.PIPELINE_VERSION}')
        print('The programs to be used in this pipline: ')
        subprocess.run([self.singularity, '--version'])
        subprocess.run([self.singularity, 'exec', self.cranger_image, 'cellranger', '--version'])