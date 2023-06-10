# Plantation Station

Plantation Station is a decentralized agent service that monitors, manages and optimizes the yield of plants and vegetables. By minting dynamic NFTs representing crops, real-time observational data is updated on-chain, providing transparency and traceability. These NFTs can be used as collateral on the PWN marketplace, enabling growers to unlock capital upfront in order to fund their operations. Additionally, individuals can invest in discounted NFTs representing real-world produce, enabling them to participate in the agricultural sector. On expiry, holders of NFTs representing yield can burn their NFT and acquire the produce. 

## Table of Contents

- [Plantation Station](#plantation-station)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [License](#license)

## Introduction

Liquidation Station aims to empower growers and investors by providing a comprehensive solution for optimizing agricultural yields. Through the creation of dynamic NFTs that represent crops, real-time observational data is stored on the blockchain, ensuring transparency and enabling efficient management of farming operations. Additionally, these NFTs can be utilized as collateral on the PWN marketplace, allowing growers to access upfront capital for funding their operations. Simultaneously, individuals have the opportunity to invest in discounted NFTs that represent real-world produce, enabling them to actively participate in the agricultural sector.

One unique feature of Liquidation Station is the ability for NFT holders to acquire the produce upon expiration. By burning their NFTs, holders can directly acquire the yield they are entitled to, creating a seamless connection between investors and the final products of sustainable farming practices.

## Features

- **Dynamic NFTs**: Mint and manage dynamic NFTs representing crops, which store real-time observational data on-chain for transparent and traceable yield monitoring.
- **NFT redemption**: NFT holders can redeem their tokens to directly acquire the produce they are entitled to, facilitating a seamless connection between investors and the final products.
- **Optimized Farming Operations**: Leverage the power of blockchain technology to optimize farming operations, enhance yield management, and support sustainable farming practices.
-  **PWN Marketplace Integration**: Utilize NFTs as collateral on the PWN marketplace, enabling growers to access upfront capital for operational funding.
- **Investment Opportunity**: Enable individuals to invest in discounted NFTs representing real-world produce, providing them with a unique way to participate in the agricultural sector.

## Requirements

pyenv

Tendermint
```bash
wget https://github.com/tendermint/tendermint/releases/download/v0.34.11/tendermint_0.34.11_linux_amd64.tar.gz

tar -xf tendermint_0.34.11_linux_amd64.tar.gz
sudo mv tendermint /usr/local/bin/tendermint
```

## Installation

To use Liquidation Station, follow the steps below:

1. Clone this repository to your local machine.

```shell
git clone https://github.com/8ball030/plantation_station.git
cd plantation_station
```

2. Setup environment
```shell
poetry shell
poetry install
```

3. Obtain package dependencies from remote IPFS registry
```shell
autonomy packages sync
```

4. Start a local Tendermint node

```shell
sudo tendermint init validator && sudo cp -r /root/.tendermint ~/  && sudo chown -R (whoami):(whoami) ~/.tendermint
tendermint start
```

5. Start the ABCI application

In a separate terminal, after dropping into venv: `poetry shell`

```shell
make run-single-agent
```


## License

This project is licensed under the [GPL 2.0 license](./LICENSE).

