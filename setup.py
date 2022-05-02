from cx_Freeze import setup, Executable

executables = [
    Executable('main.py', target_name = 'bolt')
]

setup(name="Bolt",
      version = "0.1.0",
      description = "A dead simple (and probably broken) playlist file converter for converting .m3u8 playlists to Dopamine's .m3u playlist format.",
      executables = executables)