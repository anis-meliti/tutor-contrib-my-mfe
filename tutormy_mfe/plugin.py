from glob import glob
import os
import pkg_resources

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = pkg_resources.resource_filename(
    HERE, "templates"
)

config = {
    "defaults": {
        "VERSION": __version__,
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}ansmeliti/openedx-mfe:{{ MFE_VERSION }}",
        "HOST": "apps.{{ LMS_HOST }}",
        "COMMON_VERSION": "{{ OPENEDX_COMMON_VERSION }}",
        "COURSE_AUTHORING_MFE_APP": {
            "name": "course-authoring",
            "repository": "https://github.com/anis-meliti/frontend-app-course-authoring.git",
            "port": 2001,
        },
    }
}

hooks = {
    "build-image": {
        "my-mfe": "{{ MFE_DOCKER_IMAGE }}"
    },
    "init": ["lms"]
}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        HERE, "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
