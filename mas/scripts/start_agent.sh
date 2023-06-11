set -e 


# fetch the agent from the local package registry
aea fetch zarathustra/plantation --local


# go to the new agent
cd plantation

# install the agent Note this causes a dependency issue
echo "Skipping install of aea deps" 
# aea install

# if a key exists at the default location, use it
if [ -f ~/.keys/ethereum_private_key.txt ]; then
    echo "Using existing ethereum key"
    aea add-key ethereum
else
    echo "Generating new ethereum key"
    aea generate-key ethereum && aea add-key ethereum
fi

# issue certificates for agent to agent communications
aea issue-certificates

# finally, run the agent
aea run
