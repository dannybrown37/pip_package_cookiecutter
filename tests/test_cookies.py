from pathlib import Path


def test_bake_basic_project(cookies):
    result = cookies.bake(extra_context={'project_title': 'Basic Test'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'basic_test'
    assert result.project_path.is_dir()


def test_baking_disaster_on_pre_gen_hook(cookies, caplog):
    bad_project = '??? Not a valid ! project (((name)))'
    result = cookies.bake(extra_context={'project_title': bad_project})
    assert result.exit_code == -1
    assert str(result.exception) == 'Hook script failed (exit status: 1)'
    expected_error = "pre_gen_project hook script didn't exit successfully"
    assert expected_error in caplog.text


def test_bake_cliless_project_with_post_gen_hook(cookies):
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
    main_path = Path(result.project_path) / 'tp' / 'src' / 'tp' / '__main__.py'
    assert not main_path.exists()
