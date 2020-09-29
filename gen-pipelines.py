import yaml
import argparse
import subprocess


def gen_step(target):
  return {
    "title": "{target}-test".format(target=target),
    "type": "codefresh-run",
    "arguments": {
      "PIPELINE_ID": "ngci-test/{target}".format(target=target),
      "BRANCH": "${{CF_BRANCH}}",
      "VARIABLE": [
        "CF_BRANCH=${{CF_BRANCH}}",
        "CF_REVISION=${{CF_REVISION}}",
      ],
    },
    "when": {
      "condition": {
        "all": {
          "cloneFinish": "steps.create_pipelines.result == 'success'",
        }
      }
    }
  }


def gen_pipeline(targets):
  steps = {}
  steps['main_clone'] = {
    "title": "Cloning main repo...",
    "type": "git-clone",
    "repo": "${{CF_REPO_OWNER}}/${{CF_REPO_NAME}}",
    "revision": "${{CF_REVISION}}",
    "git": "github",
  }
  for t in targets:
    steps[t] = gen_step(t)

  return {
    "version": "1.0",
    "kind": "pipeline",
    "metadata": {
      "name": 'ngci-test/pre-submit',
      "description": "PreSubmit",
      "deprecate": {},
      "project": "ngci-test",
    },
    "spec": {
      "triggers": [{
        "type": "git",
        "provider": "github",
        "name": "path-trigger",
        "repo": "rfblue2/ngci-test",
        "context": "github",
        "contexts": [],
        "events": ["push.heads"],
        "branchRegex": "/.*/gi",
        "disabled": False,
        "options": {
          "noCache": False,
          "noCfCache": False,
          "resetVolume": False,
        }
      }],
      "contexts": [],
      "variables": [],
      "mode": "parallel",
      "steps": steps,
    }
  }

if __name__ == '__main__':
  changed_files = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~1']).strip().splitlines()
  print(changed_files)

  targets = []
  if any('project1/' in str(file) for file in changed_files):
    targets.append('project1')

  if any('project2/' in str(file) for file in changed_files):
    targets.append('project2')

  # Output generated pipeline YAML
  with open("pipeline-gen.yaml", "w") as f:
    yaml.dump(gen_pipeline(targets), f)
    print(yaml.dump(gen_pipeline(targets)))