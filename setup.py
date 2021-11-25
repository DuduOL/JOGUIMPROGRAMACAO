import cx_Freeze
executables = [cx_Freeze.Executable(
    script="codigo.py", icon="assets/ironIcon.ico")]

cx_Freeze.setup(
    name="Frita Batatinha",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables=executables
)