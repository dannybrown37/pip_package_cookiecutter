from pathlib import Path


def test_chocolate_chip_cookie(cookies):
    """Straightforward new project generation"""
    result = cookies.bake(extra_context={'project_title': 'Basic Test'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'basic_test'
    assert result.project_path.is_dir()
    main_pth = Path(result.project_path) / 'src' / 'basic_test' / '__main__.py'
    assert main_pth.exists()
    venv_pth = Path(result.project_path) / '.venv'
    assert venv_pth.exists()


def test_snickerdoodle(cookies):
    """Use No CLI option and delete __main__.py with post_gen_hook"""
    result = cookies.bake(
        extra_context={
            'project_title': 'tp',
            'command_line_interface': 'No CLI',
        },
    )
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'tp'
    assert result.project_path.is_dir()
    main_pth = Path(result.project_path) / 'src' / 'tp' / '__main__.py'
    assert not main_pth.exists()



def test_baking_disaster(cookies, caplog):
    """Use an invalid project name, pre_gen_hook will fail"""
    bad_project = '??? Not a valid ! project (((name)))'
    result = cookies.bake(extra_context={'project_title': bad_project})
    assert result.exit_code == -1
    assert str(result.exception) == 'Hook script failed (exit status: 1)'
    expected_error = "pre_gen_project hook script didn't exit successfully"
    assert expected_error in caplog.text
