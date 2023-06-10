# Infra

Infra is deployed onto the hosts using the inventory file.

Dependencies must be installed in order to prepare the raspberry pi to run the necessary web3 libraries.

NOTE! The application only supports a raspberry pi4

## Installation
```bash
poetry install && poetry shell
```

```bash
ansible-playbook -i inventory.ini playbooks/rustc.yaml
ansible-playbook -i inventory.ini playbooks/setup-pi.yaml
ansible-playbook -i inventory.ini playbooks/setup-poetry.yaml
ansible-playbook -i inventory.ini playbooks/setup-services.yaml
ansible-playbook -i inventory.ini playbooks/tendermint.yaml
```

## Deployment
```bash
ansible-playbook -i inventory.ini playbooks/deploy.yaml
```
