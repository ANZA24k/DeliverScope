import pytest
from gltest.direct.loader import deploy_contract
from pathlib import Path


@pytest.fixture
def direct_deploy(direct_vm):
    def deploy(path, *args, **kwargs):
        return deploy_contract(Path(path).resolve(), direct_vm, *args, sdk_version="v0.2.16", **kwargs)

    return deploy
