# CheckerChain Subnet

Built on top of **[Bittensor Subnet Template]** & **[Commune Subnet Template]**

## Dependencies

[CommuneX library / SDK][communex] is truly the only essential dependency.
Thought, in order enable some features out of the box we have some extra
dependencies in the [pyproject.toml](./pyproject.toml) file.

## Miner

From the root of your project, you can just call **comx module serve**. For example:

```sh
comx module serve checker-chain.miner.model.Miner <name-of-your-com-key> [--subnets-whitelist <your-subnet-netuid>] \
  [--ip <text>] [--port <number>]
```

## Validator

To run the validator, just call the module in which you are executing
`validator.validation_loop()`. For example:

```sh
python3 -m checker-chain.cli <name-of-your-com-key>
```

[Bittensor Subnet Template]: https://github.com/opentensor/bittensor-subnet-template/blob/main/docs/running_on_staging.md
[communex]: https://github.com/agicommies/communex
[commune-ai]: https://communeai.org/
[Commune Subnet Template]: https://github.com/renlabs-dev/commune-subnet-template
