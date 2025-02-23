import ast


def is_dependant(source_file: str, destination: str):
    with open(source_file, "r") as f:
        source = ast.parse(f.read())

        for statement in source.body:
            if isinstance(statement, ast.Import) or isinstance(
                statement, ast.ImportFrom
            ):
                if hasattr(statement, "module") and destination in statement.module:
                    return True
                if any(name for name in statement.names if destination in name.name):
                    return True

    return False


def test_domain_core_independant_of_all_adapters():
    assert is_dependant("./tscheduler/domain/core.py", "adapters") is False


def test_domain_models_independant_of_all_adapters():
    assert is_dependant("./tscheduler/domain/models.py", "adapters") is False


def test_local_executor_depends_on_ports():
    assert is_dependant("./tscheduler/adapters/local_executor.py", "ports") is True


def test_local_storage_depends_on_ports():
    assert is_dependant("./tscheduler/adapters/local_storage.py", "ports") is True
