
# Systems Diagram

the service configuration is defined on and retrieved from the blockchain. Code required to become an agent operator can be retrieved through IPFS using the hash referenced in the service registry contract. The operators of the service may also be defined on-chain in case permissioned access is desired. The model, its parameters, and the feedback controller are stored on-chain and retrieved for initialization. Computations involving data collection, parameter optimization, and control corrections are performed off-chain in the [ABCIApp](abci_app.md). 


```mermaid
graph TB

    subgraph "Raspberry Pi"
        Sensors
        Actuators
    end

    subgraph "Agent"
        Model_Optimizer[ABCI App]
        RP_Interface[RaspberryPi Interface]
        Tendermint_Interface[Tendermint Interface]
        Blockchain_Interface[Blockchain Interface]
        
        Sensors -- "y(t)" --> RP_Interface
        RP_Interface -- Control corrections --> Actuators
        RP_Interface <--> Model_Optimizer
        Model_Optimizer <--> Tendermint_Interface
        Blockchain_Interface <--> Model_Optimizer
    end

    subgraph "Local Tendermint Consensus Network"
        Consensus_Protocol[Consensus Protocol]
        Shared_State[Shared State]
        Tendermint_Interface -- Payload:\nObservations, Predictions --> Consensus_Protocol
        Consensus_Protocol -- State Update --> Shared_State
        Shared_State -- Updated Shared State --> Tendermint_Interface
    end

    subgraph "Smart Contracts on the Blockchain"
        Parameter_Storage[Model & Parameter Storage]
        ServiceRegistry[Service Registry]
        Blockchain_Interface -- Update Parameters --> Parameter_Storage
        ServiceRegistry -- Service Configuration --> Blockchain_Interface
        Parameter_Storage -- Retrieve Model --> Blockchain_Interface
    end

    Plant -- "x(t)" --> Sensors
    Actuators -- "Δu(t)" --> Plant
```
