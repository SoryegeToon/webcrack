import pathlib

relative_directory = pathlib.Path(__file__).parent.parent  # luoshenscan代码相对路径

svscan_path_set = {
    'dict': {
        'http_username': relative_directory.joinpath(
            'dict', 'username.txt'
        ),
        'http_password': relative_directory.joinpath(
            'dict', 'password.txt'
        ),
    },
    'module_dir': relative_directory.joinpath(
        'moudle', 'poc'
    ),
    'module_path': 'moudle.poc.'
}

rule_path = {
    'ustrflag_path': relative_directory.joinpath('dict', 'u_str_flag.txt'),
    'pstrflag_path': relative_directory.joinpath('dict', 'p_str_flag.txt'),
    'uxpathflag_path': relative_directory.joinpath('dict', 'u_xpath_flag.txt'),
    'pxpathflag_path': relative_directory.joinpath('dict', 'p_xpath_flag.txt'),
}
