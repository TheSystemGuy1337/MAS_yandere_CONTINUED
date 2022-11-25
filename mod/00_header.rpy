init -990 python in mas_submod_utils:
    Submod(
        author="My Otter Self/TheSystemGuy",
        name="MAS Yandere Submod - CONTINUED",
        description="A community continued version of My Otter Self's Yandere Submod.",
        version="1.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Yandere Submod",
            user_name="my-otter-self",
            repository_name="mas_yandere",
            submod_dir="/Submods/MAS Yandere Submod",
            extraction_depth=3,
            redirected_files=(
                "README.md",
                "LICENSE.txt"
            )
        )
