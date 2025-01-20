# CheckerChain Subnet

Built on top of **[Commune Subnet Template](https://github.com/renlabs-dev/commune-subnet-template)**

## Dependencies

Currently same as the template. Read [pyproject.toml](./pyproject.toml) file.

Install the dependencies with `poetry install`. For more information on _Poetry_, visit [Poetry Docs](https://python-poetry.org/docs/#installation).

```txt
communex
typer
uvicorn
keylimiter
pydantic-settings
```

## Miner

From the root of your project, you can just call **comx module serve**. For example:

```sh
comx module serve commune-subnet-template.subnet.miner.model.Miner <name-of-your-com-key> [--subnets-whitelist <your-subnet-netuid>] \
[--ip <text>] [--port <number>]
```

## Validator

To run the validator, just call the file in which you are executing `validator.validate_loop()`. For example:

```sh
python3 -m commune-subnet-template.subnet.cli <name-of-your-com-key>
```

## Setup project

1.  Clone project

```bash
git clone https://github.com/NUMENEX/numx-subnet-commune.git
cd numx-subnet-commune
```

2.  Install the required dependencies:

```bash
poetry install
```

3.  Setup Wallet

Use communex cli to create wallet and make sure you fund them

```bash
poetry run comx key create <key_name>
poetry run comx --testnet balance run-faucet <key_name>
```

4. Setup config file Create config.ini file from config.ini.example with your actual key name

5. Register Miner/Validtor Module on Checker Chain Subnet

**Registering Miner**

> Remember ip and port args are for identifying miner and validator for now, you can put 127.0.0.1 for ip and 8000 for port

```bash
comx module register <name> <your_commune_key> --ip <your-ip-address> --port <port> --netuid <Numenex netuid>
```

Registering Validator

```bash
comx module register <name> <your_commune_key> --netuid <Numenex netuid>
```
